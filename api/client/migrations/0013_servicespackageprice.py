# Generated by Django 4.1.7 on 2023-08-28 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_remove_servicespackageprice_period_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesPackagePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Стоимость')),
                ('count_period', models.IntegerField(default=0, verbose_name='Количество периодов')),
                ('period', models.ForeignKey(blank=True, default='', help_text='Установите период за сколько будет браться цена', on_delete=django.db.models.deletion.SET_DEFAULT, to='client.period', verbose_name='В')),
                ('services_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.servicespackage', verbose_name='Пакет услуг')),
            ],
            options={
                'verbose_name': 'Цена на пакет услуг',
                'verbose_name_plural': 'Цены на пакеты услуг',
            },
        ),
    ]
