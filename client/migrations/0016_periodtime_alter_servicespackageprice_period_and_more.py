# Generated by Django 4.1.7 on 2023-08-28 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_alter_period_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, unique=True, verbose_name='Титл')),
            ],
            options={
                'verbose_name': 'Срок',
                'verbose_name_plural': 'Сроки',
            },
        ),
        migrations.AlterField(
            model_name='servicespackageprice',
            name='period',
            field=models.ForeignKey(help_text='Установите период за сколько будет браться цена', on_delete=django.db.models.deletion.CASCADE, to='client.periodtime', verbose_name='В'),
        ),
    ]
