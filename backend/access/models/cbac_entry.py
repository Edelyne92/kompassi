import logging
from datetime import datetime, timedelta
from typing import Any, Optional

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.utils.timezone import now

from core.utils import get_objects_within_period_qs, log_get_or_create
from event_log.utils import emit
from intra.constants import SUPPORTED_APPS

from ..constants import CBAC_VALID_AFTER_EVENT_DAYS

Claims = dict[str, str]
logger = logging.getLogger("kompassi")


class CBACEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cbac_entries")

    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()

    mode = models.CharField(
        max_length=1,
        choices=[("+", "Allow"), ("-", "Deny"), ("0", "Inactive")],
        default="+",
    )

    claims = HStoreField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    granted_by_group = models.ForeignKey(
        "auth.Group", on_delete=models.CASCADE, null=True, blank=True, related_name="+"
    )

    def __str__(self):
        return ", ".join(
            f"{key}={value}" for (key, value) in dict(user=self.user.username, mode=self.mode, **self.claims).items()
        )

    class Meta:
        index_together = [("user", "mode", "valid_until")]

    def save(self, *args, **kwargs):
        if not self.valid_from:
            self.valid_from = now()

        return super().save(*args, **kwargs)

    def as_dict(self) -> dict[str, Any]:
        return dict(
            user=self.user.username,
            valid_from=self.valid_from.isoformat(),
            valid_until=self.valid_until.isoformat(),
            mode=self.mode,
            claims=self.claims,
            granted_by_group=self.granted_by_group.name if self.granted_by_group else "",
        )

    @classmethod
    def get_entries(
        cls,
        user: AbstractUser,
        claims: Optional[Claims] = None,
        t: Optional[datetime] = None,
        **extra_criteria,
    ):
        # TODO make this cache all entries for the user and then filter in Python
        if not user.is_authenticated:
            return cls.objects.none()

        queryset = get_objects_within_period_qs(
            user.cbac_entries.all(),  # type: ignore
            t=t,
            start_field_name="valid_from",
            end_field_name="valid_until",
            end_field_nullable=False,
            **extra_criteria,
        )

        if claims is not None:
            queryset = queryset.filter(claims__contained_by=claims)

        return queryset

    @classmethod
    def is_allowed(cls, user: AbstractUser, claims: Claims, t: Optional[datetime] = None):
        entries = cls.get_entries(user, claims, t=t)
        return bool(entries.filter(mode="+").exists()) and not entries.filter(mode="-").exists()

    @classmethod
    def ensure_admin_group_privileges(cls, t: Optional[datetime] = None):
        from core.models import Event

        if t is None:
            t = now()

        for event in Event.objects.filter(end_time__gte=t):
            cls.ensure_admin_group_privileges_for_event(event, t=t)

    @classmethod
    def ensure_admin_group_privileges_for_event(
        cls,
        event,
        *,
        t: Optional[datetime] = None,
        request=None,
    ):
        if t is None:
            t = now()

        for app_name in SUPPORTED_APPS:
            meta = event.get_app_event_meta(app_name)

            if not meta:
                continue

            admin_group = meta.admin_group
            admin_group_members = admin_group.user_set.all()

            # remove access from those who should not have it
            entries_to_remove = cls.objects.filter(granted_by_group=admin_group).exclude(user__in=admin_group_members)
            for cbac_entry in entries_to_remove:
                emit(
                    "access.cbacentry.deleted",
                    request=request,
                    other_fields=cbac_entry.as_dict(),
                )
            entries_to_remove.delete()

            # add access to those who should have it but do not yet have
            for user in admin_group_members:
                cbac_entry, created = cls.objects.get_or_create(
                    user=user,
                    granted_by_group=admin_group,
                    defaults=dict(
                        valid_from=t,
                        valid_until=event.end_time + timedelta(CBAC_VALID_AFTER_EVENT_DAYS),
                        claims={
                            "organization": event.organization.slug,
                            # omit "event" to give permissions also to other events of same organizer
                            # "event": event.slug,
                            "app": app_name,
                        },
                        created_by=request.user if request else None,
                    ),
                )
                log_get_or_create(logger, cbac_entry, created)
                if created:
                    emit(
                        "access.cbacentry.created",
                        request=request,
                        other_fields=cbac_entry.as_dict(),
                    )

    @classmethod
    def prune_expired(cls, *, t: Optional[datetime] = None, request=None):
        if t is None:
            t = now()

        expired_entries = cls.objects.filter(valid_until__lte=t)
        logger.info("Removing %d CBAC entries expired on or before %s", expired_entries.count(), t.isoformat())

        for cbac_entry in expired_entries:
            emit(
                "access.cbacentry.deleted",
                request=request,
                other_fields=cbac_entry.as_dict(),
            )

        expired_entries.delete()
