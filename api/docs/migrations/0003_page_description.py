# Generated by Django 4.1.7 on 2023-08-28 20:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_alter_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Описание'),
        ),
    ]
