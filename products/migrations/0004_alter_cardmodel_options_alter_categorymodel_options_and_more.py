# Generated by Django 4.1.7 on 2023-05-07 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_categorymodel_user_account_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardmodel',
            options={'verbose_name': 'Тип комнаты', 'verbose_name_plural': 'Тип комнаты'},
        ),
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Тип мебели', 'verbose_name_plural': 'Тип мебели'},
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='user_account_id',
        ),
    ]
