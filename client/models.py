from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from .service.date import DateHelp


# ===========
# Клиенты
# ===========
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


# ===========
# Пакеты услуг
# ===========
class ServicesPackage(models.Model):
    title = models.CharField('Название', max_length=128, unique=True)
    content = RichTextUploadingField(verbose_name='Текст', default='', blank=True)

    class Meta:
        verbose_name = "Пакет услуг"
        verbose_name_plural = "Пакеты услуг"

    def __str__(self):
        return self.title


class Period(models.Model):
    title = models.CharField('Титл', max_length=16, unique=True)

    class Meta:
        verbose_name = "Срок"
        verbose_name_plural = "Сроки"

    def __str__(self):
        return self.title


class ServicesPackagePrice(models.Model):
    services_package = models.ForeignKey(ServicesPackage, verbose_name="Пакет услуг", on_delete=models.CASCADE)
    price = models.FloatField('Стоимость', default=0)
    period = models.ForeignKey(Period, verbose_name="В", on_delete=models.CASCADE,
                               help_text="Установите период за сколько будет браться цена")
    count_period = models.IntegerField('Количество периодов', default=0)

    class Meta:
        verbose_name = "Цена на пакет услуг"
        verbose_name_plural = "Цены на пакеты услуг"

    def __str__(self):
        norm_form = DateHelp().get_norm_form(int(str(self.count_period)), str(self.period))
        return f"{self.services_package} [{self.price} в {self.period}, на {norm_form}]"


# ===========
# Запрос клиента
# ===========
class BusinessRequest(models.Model):
    title = models.CharField('Название', max_length=128)
    description = RichTextUploadingField(verbose_name='Описание')
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    services_package_price = models.ManyToManyField(ServicesPackagePrice, verbose_name="Пакет услуг",
                                                    related_name="package")

    class Meta:
        verbose_name = "Запрос клиента"
        verbose_name_plural = "Запросы клиентов"

    def __str__(self):
        packages = [str(el) for el in self.services_package_price.all()]
        return f"{self.title} - {self.client} {packages}"
