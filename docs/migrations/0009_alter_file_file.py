# Generated by Django 4.1.7 on 2023-08-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0008_remove_file_link_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='docs/file/', verbose_name='Файл'),
        ),
    ]
