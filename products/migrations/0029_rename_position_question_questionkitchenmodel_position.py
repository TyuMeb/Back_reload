# Generated by Django 4.1.7 on 2023-05-25 07:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0028_questionkitchenmodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="questionkitchenmodel",
            old_name="position_question",
            new_name="position",
        ),
    ]
