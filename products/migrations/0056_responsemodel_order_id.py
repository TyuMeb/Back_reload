# Generated by Django 4.1.7 on 2023-06-23 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_ordermodel_options'),
        ('products', '0055_remove_responsemodel_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsemodel',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.ordermodel'),
        ),
    ]
