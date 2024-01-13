# Generated by Django 4.2.6 on 2023-11-08 19:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0038_alter_person_discord_handle"),
        ("forms", "0008_eventform_language_globalform_language"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventform",
            name="active",
        ),
        migrations.RemoveField(
            model_name="eventform",
            name="login_required",
        ),
        migrations.RemoveField(
            model_name="eventform",
            name="standalone",
        ),
        migrations.RemoveField(
            model_name="globalform",
            name="active",
        ),
        migrations.RemoveField(
            model_name="globalform",
            name="login_required",
        ),
        migrations.RemoveField(
            model_name="globalform",
            name="standalone",
        ),
        migrations.AddField(
            model_name="eventformresponse",
            name="ip_address",
            field=models.CharField(blank=True, default="", max_length=48, verbose_name="IP address"),
        ),
        migrations.AddField(
            model_name="globalformresponse",
            name="ip_address",
            field=models.CharField(blank=True, default="", max_length=48, verbose_name="IP address"),
        ),
        migrations.CreateModel(
            name="GlobalSurvey",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("active", models.BooleanField(default=True)),
                (
                    "standalone",
                    models.BooleanField(
                        default=True,
                        help_text="Stand-alone forms can be used via the generic form views whereas non-stand-alone forms can only be accessed from some other facility.",
                        verbose_name="Stand-alone",
                    ),
                ),
                (
                    "login_required",
                    models.BooleanField(
                        default=False,
                        help_text="This switch only takes effect in a stand-alone context. In non-stand-alone contexts the use case will direct whether or not login is required.",
                        verbose_name="Login required",
                    ),
                ),
                (
                    "active_from",
                    models.DateTimeField(
                        blank=True,
                        help_text="The form will be available from this date onwards. If not set, the form will not be available.",
                        null=True,
                        verbose_name="active from",
                    ),
                ),
                (
                    "active_until",
                    models.DateTimeField(
                        blank=True,
                        help_text="The form will be available until this date. If not set, the form will be available indefinitely provided that active_from is set and has passed.",
                        null=True,
                        verbose_name="active until",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                        max_length=255,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                                regex="[a-z0-9-]+",
                            )
                        ],
                        verbose_name="Tekninen nimi",
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        help_text="The form will be available in these languages. Each language can have its own set of fields. There must be exactly one form per supported language.",
                        to="forms.globalform",
                        verbose_name="language versions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EventSurvey",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("active", models.BooleanField(default=True)),
                (
                    "standalone",
                    models.BooleanField(
                        default=True,
                        help_text="Stand-alone forms can be used via the generic form views whereas non-stand-alone forms can only be accessed from some other facility.",
                        verbose_name="Stand-alone",
                    ),
                ),
                (
                    "login_required",
                    models.BooleanField(
                        default=False,
                        help_text="This switch only takes effect in a stand-alone context. In non-stand-alone contexts the use case will direct whether or not login is required.",
                        verbose_name="Login required",
                    ),
                ),
                (
                    "active_from",
                    models.DateTimeField(
                        blank=True,
                        help_text="The form will be available from this date onwards. If not set, the form will not be available.",
                        null=True,
                        verbose_name="active from",
                    ),
                ),
                (
                    "active_until",
                    models.DateTimeField(
                        blank=True,
                        help_text="The form will be available until this date. If not set, the form will be available indefinitely provided that active_from is set and has passed.",
                        null=True,
                        verbose_name="active until",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                                regex="[a-z0-9-]+",
                            )
                        ],
                        verbose_name="Tekninen nimi",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="surveys", to="core.event"
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        help_text="The form will be available in these languages. Each language can have its own set of fields. There must be exactly one form per supported language.",
                        to="forms.eventform",
                        verbose_name="language versions",
                    ),
                ),
            ],
            options={
                "unique_together": {("event", "slug")},
            },
        ),
    ]
