# Generated by Django 4.1.7 on 2023-08-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_servicespackage_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessrequest',
            options={'verbose_name': 'Запрос клиента', 'verbose_name_plural': 'Запросы клиентов'},
        ),
        migrations.RemoveField(
            model_name='businessrequest',
            name='services_package',
        ),
        migrations.RemoveField(
            model_name='servicespackage',
            name='price',
        ),
        migrations.CreateModel(
            name='ServicesPackagePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Стоимость')),
                ('services_package', models.ManyToManyField(related_name='services_package', to='client.servicespackage', verbose_name='Пакет услуг')),
            ],
            options={
                'verbose_name': 'Цена на пакет услуг',
                'verbose_name_plural': 'Цены на пакеты услуг',
            },
        ),
        migrations.AddField(
            model_name='businessrequest',
            name='services_package_price',
            field=models.ManyToManyField(related_name='services_package_price', to='client.servicespackageprice', verbose_name='Пакет услуг'),
        ),
    ]
