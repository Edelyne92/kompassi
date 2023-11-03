# Generated by Django 4.0.6 on 2022-08-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0031_alter_ticketseventmeta_event_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="accommodationinformation",
            name="is_present",
            field=models.BooleanField(default=False, verbose_name="Läsnäoleva"),
        ),
        migrations.AddField(
            model_name="accommodationinformation",
            name="room_name",
            field=models.CharField(blank=True, default="", max_length=63, verbose_name="Majoitustila"),
        ),
    ]