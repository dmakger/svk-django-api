from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# ===========
# Меню
# ===========
class Menu(models.Model):
    path = models.CharField('Путь', max_length=64, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.title


class SubMenu(models.Model):
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE, verbose_name='Меню')
    path = models.CharField('Путь', max_length=64, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = "Подменю"
        verbose_name_plural = "Подменю"

    def __str__(self):
        return f"[{self.menu.title}] {self.title}"


class File(models.Model):
    link = models.CharField('Ссылка на файл', max_length=64, unique=True)
    file = models.FilePathField('Файл', path='docs/')
    title = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.title


class Page(models.Model):
    submenu = models.ForeignKey(to=SubMenu, on_delete=models.CASCADE, verbose_name='Подменю')
    path = models.CharField('Путь', max_length=64, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)
    content = RichTextUploadingField(verbose_name='Содержимое', blank=True, default='')
    files = models.ManyToManyField(File, verbose_name="Файлы", related_name="files")

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return f"{self.title} [{self.submenu.menu} {self.submenu}]"
