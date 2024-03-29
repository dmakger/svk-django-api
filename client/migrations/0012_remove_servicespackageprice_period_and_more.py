# Generated by Django 4.1.7 on 2023-08-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_alter_servicespackageprice_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicespackageprice',
            name='period',
        ),
        migrations.RemoveField(
            model_name='servicespackageprice',
            name='services_package',
        ),
        migrations.AlterField(
            model_name='businessrequest',
            name='services_package_price',
            field=models.ManyToManyField(related_name='services_package_price', to='client.servicespackage', verbose_name='Пакет услуг'),
        ),
        migrations.DeleteModel(
            name='ServicesPackagePrice',
        ),
    ]
