# Generated by Django 4.0.6 on 2022-08-23 11:29

import django.db.models.deletion
from django.db import migrations, models

import access.utils


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0037_alter_organization_panel_css_class"),
        ("paikkala", "0016_zone_ordering"),
        ("ropecon2021", "0002_alter_signupextra_event_alter_signupextra_person"),
        ("ropecon2019", "0005_alter_signupextra_event_alter_signupextra_person"),
        ("programme", "0108_auto_20220313_1906"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programme",
            name="ropecon2019_blocked_time_slots",
            field=models.ManyToManyField(
                blank=True,
                help_text="Tell us when you <strong>can not run</strong> your game. You can write more specific requests in the <em>other information</em> field below (e.g. <em>I'd like to run my game late in the evening</em>), but here we want information about limitations set by for example work or bus schedules (for example if you need to leave the venue by 11 PM to get to your accommodation in time).",
                related_name="+",
                to="ropecon2019.timeslot",
                verbose_name="When are you unable to run your game?",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="ropecon2019_preferred_time_slots",
            field=models.ManyToManyField(
                blank=True,
                help_text="When would you like to host your game program? Check the times when you would like to host your game program. If you have more specific needs regarding the timing, please let us know in the Comments field below. We do not restrict your desired times, but we reserve the right to make changes. For example, we would rather have tournaments one after another than at the same time.",
                related_name="+",
                to="ropecon2019.timeslot",
                verbose_name="time preferences",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="ropecon2021_blocked_time_slots",
            field=models.ManyToManyField(
                blank=True,
                help_text="Select the times when you are <b>NOT able</b> to run your larp. In other words, leave the times that you would be able to run your larp unselected!<br/>If you have a more specific request in mind regarding your schedule (for example, you would like to run your larp late at night), please let us know in the Comments section below.<br/>In this section, we would like to know more about how work or volunteer shifts, public transport schedules and other factors might be impacting your schedule. For example, if you need to leave the venue by 11pm to be able to catch the last bus to your accommodation.",
                related_name="+",
                to="ropecon2021.timeslot",
                verbose_name="When are you NOT able to run your larp?",
            ),
        ),
        migrations.AlterField(
            model_name="programmeeventmeta",
            name="event",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="%(class)s",
                serialize=False,
                to="core.event",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="paikkala_room",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="paikkala.room"
            ),
        ),
        migrations.CreateModel(
            name="SpecialReservation",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(default=access.utils.generate_machine_password, max_length=63, unique=True)),
                ("row_name", models.CharField(max_length=255)),
                ("seat_number", models.CharField(default="Numeroimaton", max_length=255)),
                ("description", models.TextField()),
                ("program", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="paikkala.program")),
                ("zone", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="paikkala.zone")),
            ],
        ),
    ]
