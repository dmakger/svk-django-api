from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# ===========
# Меню
# ===========
class Menu(models.Model):
    path = models.CharField('Путь', max_length=64, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)
    isVisible = models.BooleanField('Отображать меню', default=False)
    number = models.IntegerField('Порядковый номер', default=999)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField('Файл', upload_to='docs/file/')
    title = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.title


class Page(models.Model):
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE, verbose_name='Меню')
    path = models.CharField('Путь', max_length=64, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)
    description = RichTextUploadingField(verbose_name='Описание', blank=True, default='')
    content = RichTextUploadingField(verbose_name='Содержимое', blank=True, default='')
    files = models.ManyToManyField(File, verbose_name="Файлы", related_name="files", default='', blank=True)
    isVisible = models.BooleanField('Отображать страницу', default=False)
    number = models.IntegerField('Порядковый номер', default=999)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return f"{self.title} [{self.menu}]"
