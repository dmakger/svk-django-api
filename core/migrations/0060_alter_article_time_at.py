# Generated by Django 4.1.7 on 2023-09-30 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_alter_article_time_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 9, 30, 18, 14, 42, 367060), verbose_name='Время создания'),
        ),
    ]
