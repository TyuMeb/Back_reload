# Generated by Django 4.1.7 on 2023-05-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0007_useraccount_person_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="is_partner",
            field=models.BooleanField(default=False),
        ),
    ]
