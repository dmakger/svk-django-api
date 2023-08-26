from django.contrib import admin

# Register your models here.
from .models import Client, SocialNetwork, ServicesPackage, BusinessRequest

admin.site.register(SocialNetwork)
admin.site.register(Client)
admin.site.register(ServicesPackage)
admin.site.register(BusinessRequest)
