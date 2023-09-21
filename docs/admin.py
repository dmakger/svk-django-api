from django.contrib import admin

from .models import Menu, File, Page

# Меню
admin.site.register(Menu)

# Страница
admin.site.register(File)
admin.site.register(Page)
