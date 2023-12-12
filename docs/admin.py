from django.contrib import admin

from .models import Menu, File, Page


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'path', 'isVisible', 'number']


class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'file']


class PageAdmin(admin.ModelAdmin):
    list_display = ['menu', 'path', 'title', 'description', 'formatted_files', 'isVisible', 'number']

    def formatted_files(self, obj):
        return ', '.join(file.title for file in obj.files.all())

    formatted_files.short_description = 'File'


# Меню
admin.site.register(Menu, MenuAdmin)

# Страница
admin.site.register(File, FileAdmin)
admin.site.register(Page, PageAdmin)
