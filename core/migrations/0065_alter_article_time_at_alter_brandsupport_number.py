# Generated by Django 4.1.7 on 2023-11-05 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_alter_article_time_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 11, 5, 17, 0, 16, 14742), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='brandsupport',
            name='number',
            field=models.IntegerField(default=999, verbose_name='Порядковый номер'),
        ),
    ]
