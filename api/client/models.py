from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class SocialNetwork(models.Model):
    link = models.CharField('Ссылка', max_length=128)

    class Meta:
        verbose_name = "Соц. сеть"
        verbose_name_plural = "Соц. сети"

    def __str__(self):
        return f"{self.link}"


class Client(models.Model):
    username = models.CharField('Имя', max_length=128)
    number_phone = models.CharField('Номер телефона', max_length=16, unique=True)
    email = models.CharField('Email', max_length=64, unique=True)
    communication = models.ManyToManyField(SocialNetwork, verbose_name="Соц. сеть", related_name="communication")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.username} [{self.number_phone}]"


class ServicesPackage(models.Model):
    title = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = "Пакет услуг"
        verbose_name_plural = "Пакеты услуг"

    def __str__(self):
        return self.title


class BusinessRequest(models.Model):
    title = models.CharField('Название', max_length=128)
    description = RichTextUploadingField(verbose_name='Описание')
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    services_package = models.ManyToManyField(ServicesPackage, verbose_name="Пакет услуг",
                                              related_name="services_package")

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

    def __str__(self):
        return f"{self.title} - {self.client} [{self.services_package}]"
