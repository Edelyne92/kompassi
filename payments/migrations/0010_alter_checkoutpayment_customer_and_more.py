# Generated by Django 4.2.7 on 2023-11-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0009_delete_paymentseventmeta"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkoutpayment",
            name="customer",
            field=models.JSONField(editable=False),
        ),
        migrations.AlterField(
            model_name="checkoutpayment",
            name="items",
            field=models.JSONField(editable=False),
        ),
    ]