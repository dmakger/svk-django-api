# Generated by Django 4.1.7 on 2023-09-05 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_alter_article_time_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 9, 5, 23, 15, 20, 575612), verbose_name='Время создания'),
        ),
    ]