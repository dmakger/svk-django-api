# Generated by Django 4.1.7 on 2023-08-28 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_article_time_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 8, 28, 15, 54, 54, 23423), verbose_name='Время создания'),
        ),
    ]
