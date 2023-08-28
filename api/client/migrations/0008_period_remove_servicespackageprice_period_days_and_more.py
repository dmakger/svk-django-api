# Generated by Django 4.1.7 on 2023-08-28 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_servicespackageprice_period_days_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Срок',
                'verbose_name_plural': 'Сроки',
            },
        ),
        migrations.RemoveField(
            model_name='servicespackageprice',
            name='period_days',
        ),
        migrations.AddField(
            model_name='servicespackageprice',
            name='count_period',
            field=models.IntegerField(default=0, verbose_name='Количество периодов'),
        ),
        migrations.AddField(
            model_name='servicespackageprice',
            name='period',
            field=models.ForeignKey(default=1, help_text='Установите период за сколько будет браться цена', on_delete=django.db.models.deletion.CASCADE, to='client.period', verbose_name='В'),
            preserve_default=False,
        ),
    ]