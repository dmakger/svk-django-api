# Generated by Django 4.1.7 on 2023-11-05 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_alter_article_time_at_alter_brandsupport_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time_at',
            field=models.TimeField(default=datetime.datetime(2023, 11, 5, 17, 33, 58, 618350), verbose_name='Время создания'),
        ),
    ]
