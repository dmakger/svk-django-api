# Generated by Django 4.1.7 on 2023-08-24 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_date_creation_article_date_at_article_time_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 8, 25, 1, 16, 48, 456723), verbose_name='Время создания'),
        ),
    ]
