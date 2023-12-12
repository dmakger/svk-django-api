from django.contrib import admin

from .models import Client, SocialNetwork, BusinessRequest, ServicesPackage, Period, ServicesPackagePrice


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['link']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['username', 'number_phone', 'email', 'formatted_communication']

    def formatted_communication(self, obj):
        return ', '.join(str(it) for it in obj.communication.all())

    formatted_communication.short_description = 'Client'


class ServicesPackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']


class PeriodAdmin(admin.ModelAdmin):
    list_display = ['title']


class ServicesPackagePriceAdmin(admin.ModelAdmin):
    list_display = ['services_package', 'price', 'period', 'count_period']


class BusinessRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'client', 'formatted_services_package_price']

    def formatted_services_package_price(self, obj):
        return ', '.join(str(it) for it in obj.services_package_price.all())

    formatted_services_package_price.short_description = 'BusinessRequest'


# Клиенты
admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Client, ClientAdmin)

# Пакеты услуг
admin.site.register(ServicesPackage, ServicesPackageAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(ServicesPackagePrice, ServicesPackagePriceAdmin)

# Запрос клиента
admin.site.register(BusinessRequest, BusinessRequestAdmin)
