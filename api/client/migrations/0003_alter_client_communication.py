# Generated by Django 4.1.7 on 2023-08-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_servicespackage_socialnetwork_businessrequest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='communication',
            field=models.ManyToManyField(related_name='communication', to='client.socialnetwork', verbose_name='Соц. сеть'),
        ),
    ]
