# Generated by Django 4.1.7 on 2023-06-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0017_alter_sellerdata_options_alter_useraccount_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useraccount",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
