import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class BrandSupport(models.Model):
    path = models.CharField('Путь', max_length=128, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)
    description = RichTextUploadingField(verbose_name='Описание')
    link = models.CharField('Ссылка на страницу бренда', max_length=128)
    logo_image = models.ImageField("Логотип", upload_to='brand_support/logo/')

    class Meta:
        verbose_name = "Поддержка бренда"
        verbose_name_plural = "Поддержка бренда"

    def __str__(self):
        return self.title


class BrandPartner(models.Model):
    path = models.CharField('Путь', max_length=128, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)
    description = RichTextUploadingField(verbose_name='Описание')
    link = models.CharField('Ссылка на страницу бренда', max_length=128)
    logo_image = models.ImageField("Логотип", upload_to='brand_partner/logo/')

    class Meta:
        verbose_name = "Партнёр бренда"
        verbose_name_plural = "Партнёры бренда"

    def __str__(self):
        return self.title


class Writer(models.Model):
    path = models.CharField('Путь', max_length=128, unique=True)
    firstname = models.CharField('Имя', max_length=128)
    lastname = models.CharField('Фамилия', max_length=128, null=True, blank=True)
    pastname = models.CharField('Отчество', max_length=128, null=True, blank=True)
    description = RichTextUploadingField(verbose_name='Описание')
    avatar_image = models.ImageField("Аватар", upload_to='writer/avatar/', null=True, blank=True)
    number_articles = models.IntegerField("Количество статей", default=0)

    class Meta:
        verbose_name = "Писатель"
        verbose_name_plural = "Писатели"

    def __str__(self):
        return f"{self.lastname} {self.firstname} {self.pastname}"


class Tag(models.Model):
    path = models.CharField('Путь', max_length=128, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)
    description = RichTextUploadingField(verbose_name='Описание')

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title


class Article(models.Model):
    writer = models.ForeignKey(to=Writer, on_delete=models.CASCADE, verbose_name='Писатель')
    brand = models.ForeignKey(to=BrandPartner, on_delete=models.CASCADE, verbose_name='Бренд')
    path = models.CharField('Путь', max_length=128, unique=True)
    title = models.CharField('Название', max_length=128, unique=True)
    description = RichTextUploadingField(verbose_name='Описание')
    preview_image = models.ImageField("Обложка", upload_to='article/preview/', blank=True, null=True)
    time_at = models.TimeField('Время создания', default=datetime.datetime.now())
    date_at = models.DateField('Дата создания', default=datetime.date.today)
    content = RichTextUploadingField(verbose_name='Контент')
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name="tags")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"[{self.date_at}] -> {self.title}"

