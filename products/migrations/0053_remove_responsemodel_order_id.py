# Generated by Django 4.1.7 on 2023-06-23 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0052_responsemodel_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsemodel',
            name='order_id',
        ),
    ]
