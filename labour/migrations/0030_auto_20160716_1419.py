# Generated by Django 1.9.5 on 2016-07-16 11:19


import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0023_auto_20160704_2155"),
        ("labour", "0029_auto_20160608_2309"),
    ]

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "slug",
                    models.CharField(
                        help_text='Tekninen nimi eli "slug" n\xe4kyy URL-osoitteissa. Sallittuja merkkej\xe4 ovat pienet kirjaimet, numerot ja v\xe4liviiva. Teknist\xe4 nime\xe4 ei voi muuttaa luomisen j\xe4lkeen.',
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Tekninen nimi saa sis\xe4lt\xe4\xe4 vain pieni\xe4 kirjaimia, numeroita sek\xe4 v\xe4liviivoja.",
                                regex="[a-z0-9-]+",
                            )
                        ],
                        verbose_name="Tekninen nimi",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Will be displayed at the top of the survey page.",
                        max_length=255,
                        verbose_name="Title",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Will be displayed at the top of the survey page.", verbose_name="Description"
                    ),
                ),
                ("active_from", models.DateTimeField(blank=True, null=True, verbose_name="Active from")),
                ("active_until", models.DateTimeField(blank=True, null=True, verbose_name="Active until")),
                (
                    "form_class_path",
                    models.CharField(
                        help_text="A reference to the form that is used as the survey form.",
                        max_length=255,
                        verbose_name="Form path",
                    ),
                ),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.Event")),
            ],
            options={
                "verbose_name": "Survey",
                "verbose_name_plural": "Surveys",
            },
        ),
        migrations.AlterField(
            model_name="alternativesignupform",
            name="active_from",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Active from"),
        ),
        migrations.AlterField(
            model_name="alternativesignupform",
            name="active_until",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Active until"),
        ),
        migrations.AlterUniqueTogether(
            name="survey",
            unique_together={("event", "slug")},
        ),
    ]
