# Generated by Django 4.1.7 on 2023-05-21 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orderoffer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderoffer',
            name='seller_id',
        ),
    ]
