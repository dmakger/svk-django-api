# Generated by Django 4.1.7 on 2023-09-30 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_alter_article_time_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 9, 30, 17, 18, 26, 209243), verbose_name='Время создания'),
        ),
    ]
