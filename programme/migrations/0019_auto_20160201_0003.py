# Generated by Django 1.9.1 on 2016-01-31 22:03


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0018_auto_20160131_2044"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="role",
            options={
                "ordering": ("personnel_class__event", "title"),
                "verbose_name": "role",
                "verbose_name_plural": "roles",
            },
        ),
        migrations.RemoveField(
            model_name="role",
            name="priority",
        ),
        migrations.AlterField(
            model_name="role",
            name="personnel_class",
            field=models.ForeignKey(
                blank=True,
                help_text="The personnel class for the programme hosts that have this role.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="labour.PersonnelClass",
                verbose_name="Personnel class",
            ),
        ),
    ]
