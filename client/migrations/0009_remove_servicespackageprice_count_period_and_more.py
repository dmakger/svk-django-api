# Generated by Django 4.1.7 on 2023-08-28 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_period_remove_servicespackageprice_period_days_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicespackageprice',
            name='count_period',
        ),
        migrations.RemoveField(
            model_name='servicespackageprice',
            name='period',
        ),
    ]
