# Generated by Django 4.1.7 on 2023-05-02 19:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0002_personalclientdata"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personalclientdata",
            name="user_account",
        ),
    ]
