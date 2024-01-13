# Generated by Django 1.9.1 on 2016-01-29 19:40


import logging

from django.db import migrations

logger = logging.getLogger("kompassi")


def populate_denormalized_fields(apps, schema_editor):
    Badge = apps.get_model("badges", "badge")

    for badge in Badge.objects.all().select_related("person"):
        if not badge.person:
            logger.warning("Badge %s does not have a Person", badge)

        if badge.person.preferred_name_display_style:
            name_display_style = badge.person.preferred_name_display_style
        else:
            if badge.person.nick:
                name_display_style = "firstname_nick_surname"
            else:
                name_display_style = "firstname_surname"

        badge.first_name = badge.person.first_name
        badge.is_first_name_visible = "firstname" in name_display_style
        badge.surname = badge.person.surname
        badge.is_surname_visible = "surname" in name_display_style
        badge.nick = badge.person.nick
        badge.is_nick_visible = "nick" in name_display_style

        badge.save()


class Migration(migrations.Migration):
    dependencies = [
        ("badges", "0009_add_denormalized_fields"),
    ]

    operations = [
        migrations.RunPython(populate_denormalized_fields, elidable=True),
    ]
