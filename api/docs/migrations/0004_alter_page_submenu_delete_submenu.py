# Generated by Django 4.1.7 on 2023-08-28 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_page_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='submenu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.menu', verbose_name='Подменю'),
        ),
        migrations.DeleteModel(
            name='SubMenu',
        ),
    ]
