from django.contrib import admin
from bugs.models import Bug

# Обращение пользователя насчет багов
admin.site.register(Bug)
