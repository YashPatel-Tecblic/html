# Generated by Django 4.2 on 2023-04-18 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_rename_expiry_date_payment2_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment2",
            name="checkbox",
        ),
    ]
