# Generated by Django 4.1.7 on 2023-05-26 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_alter_questionoptionsmodel_question_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionOptionsModel',
            new_name='QuestionOptionsKitchenModel',
        ),
    ]
