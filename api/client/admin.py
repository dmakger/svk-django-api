from django.contrib import admin

from .models import Client, SocialNetwork, BusinessRequest, ServicesPackage, Period, ServicesPackagePrice

# Клиенты
admin.site.register(SocialNetwork)
admin.site.register(Client)

# Пакеты услуг
admin.site.register(ServicesPackage)
admin.site.register(Period)
admin.site.register(ServicesPackagePrice)

# Запрос клиента
admin.site.register(BusinessRequest)
