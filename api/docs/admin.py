from django.contrib import admin

from .models import Menu, SubMenu, \
                    File, Page

# Меню
admin.site.register(Menu)
admin.site.register(SubMenu)

# Страница
admin.site.register(File)
admin.site.register(Page)