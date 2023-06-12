# Generated by Django 4.1.7 on 2023-05-21 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderimagemodel'),
        ('products', '0026_delete_productimagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.ordermodel'),
        ),
    ]