# Generated by Django 4.1.7 on 2023-05-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0006_personalclientdata_user_account_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="person_address",
            field=models.CharField(max_length=200, null=True, verbose_name="Адрес"),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="person_created",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата создания аккаунта"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="person_rating",
            field=models.IntegerField(null=True, verbose_name="Рейтинг клиента"),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="person_telephone",
            field=models.CharField(
                max_length=20, null=True, verbose_name="Номер телефона"
            ),
        ),
    ]
