# Generated by Django 4.1.7 on 2023-08-28 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_alter_article_time_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 8, 28, 16, 15, 45, 190209), verbose_name='Время создания'),
        ),
    ]
