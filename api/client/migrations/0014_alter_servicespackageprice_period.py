# Generated by Django 4.1.7 on 2023-08-28 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_servicespackageprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespackageprice',
            name='period',
            field=models.ForeignKey(help_text='Установите период за сколько будет браться цена', on_delete=django.db.models.deletion.CASCADE, to='client.period', verbose_name='В'),
        ),
    ]