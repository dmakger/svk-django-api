from django.db import models


# ===========
# Обращение пользователя насчет багов
# ===========
class Bug(models.Model):
    page = models.CharField('Страница', max_length=128)
    calling_error = models.TextField('Вызов ошибки')
    description = models.TextField('Описание ошибки')

    class Meta:
        verbose_name = "Ошибка на сайте"
        verbose_name_plural = "Ошибки на сайте"

    def __str__(self):
        return f"{self.page}"
