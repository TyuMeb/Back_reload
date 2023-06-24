# Generated by Django 4.1.7 on 2023-05-21 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0006_remove_orderoffer_seller_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderoffer',
            name='user_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
