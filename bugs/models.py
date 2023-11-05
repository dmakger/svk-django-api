import re

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# ===========
# Обращение пользователя насчет багов
# ===========
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from api import settings


class Bug(models.Model):
    page = models.CharField('Страница', max_length=128)
    calling_error = models.TextField('Вызов ошибки')
    description = models.TextField('Описание ошибки')

    class Meta:
        verbose_name = "Ошибка на сайте"
        verbose_name_plural = "Ошибки на сайте"

    def __str__(self):
        return f"{self.page}"


# ===========
# Тела писем
# ===========
class MailFooter(models.Model):
    title = models.CharField('Название', max_length=128, help_text='Не будет отображаться в письме')
    content = RichTextUploadingField(verbose_name='Содержание письма')

    class Meta:
        verbose_name = "Подвал письма"
        verbose_name_plural = "Подвал писем"

    def __str__(self):
        return f"{self.title}"


# ===========
# Тела писем
# ===========
class MailBody(models.Model):
    title = models.CharField('Титульник', max_length=128)
    content = RichTextUploadingField(verbose_name='Содержание письма')
    footer = models.ForeignKey(MailFooter, on_delete=models.SET_NULL, verbose_name='Подвал письма', null=True)

    class Meta:
        verbose_name = "Тело письма"
        verbose_name_plural = "Тела писем"

    def __str__(self):
        return f"{self.title}"
