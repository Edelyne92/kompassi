# Generated by Django 4.2.9 on 2024-01-16 11:34

from django.conf import settings
from django.db import migrations


def forwards(apps, schema_editor):
    """
    Remove deny and inactive CBAC entries.
    """
    CBACEntry = apps.get_model("access", "CBACEntry")
    CBACEntry.objects.filter(mode="-").delete()
    CBACEntry.objects.filter(mode="0").delete()


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("access", "0019_auto_20211013_1702"),
    ]

    operations = [
        migrations.RunPython(forwards),
        migrations.AlterIndexTogether(
            name="cbacentry",
            index_together={("user", "valid_until")},
        ),
        migrations.RemoveField(
            model_name="cbacentry",
            name="mode",
        ),
    ]