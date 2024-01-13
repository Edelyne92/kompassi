# Generated by Django 2.1.8 on 2019-05-17 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0089_auto_20190305_1945"),
    ]

    operations = [
        migrations.AddField(
            model_name="alternativeprogrammeform",
            name="role",
            field=models.ForeignKey(
                blank=True,
                help_text="If set, programme hosts entering programme using this form will by default gain this role.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="programme.Role",
                verbose_name="Role",
            ),
        ),
    ]
