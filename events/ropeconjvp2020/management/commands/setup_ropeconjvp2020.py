from datetime import datetime

from django.core.management.base import BaseCommand

from dateutil.tz import tzlocal


class Command(BaseCommand):
    def handle(self, *args, **opts):
        from core.models import Event, Organization, Venue
        from enrollment.models import EnrollmentEventMeta

        tz = tzlocal()
        organization = Organization.objects.get(slug='ropecon-ry')
        venue, unused = Venue.objects.get_or_create(name='Ilmoitetaan myöhemmin', defaults=dict(
            name_inessive='Ilmoitetaan myöhemmin',
        ))
        event, unused = Event.objects.get_or_create(
            slug='ropeconjvp2020',
            defaults=dict(
                public=False,
                name='Ropeconin JV-peruskurssi 2020',
                name_genitive='Ropeconin JV-peruskurssin',
                name_illative='Ropeconin JV-peruskurssille',
                name_inessive='Ropeconin JV-peruskurssilla',
                homepage_url='http://ropecon.fi/hallitus',
                organization=organization,
                start_time=datetime(2020, 3, 14, 11, 0, tzinfo=tz),
                end_time=datetime(2020, 3, 14, 19, 0, tzinfo=tz),
                venue=venue,
            )
        )

        admin_group, = EnrollmentEventMeta.get_or_create_groups(event, ['admins'])

        EnrollmentEventMeta.objects.get_or_create(
            event=event,
            defaults=dict(
                admin_group=admin_group,
                form_class_path='events.ropeconjvp2020.forms:EnrollmentForm',
                is_participant_list_public=False,
                is_official_name_required=True,
            ),
        )
