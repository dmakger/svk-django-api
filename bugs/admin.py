from django.contrib import admin

from bugs.models import Bug, MailBody, MailFooter


class BugAdmin(admin.ModelAdmin):
    list_display = ['page', 'calling_error', 'description']


class MailFooterAdmin(admin.ModelAdmin):
    list_display = ['title']


class MailBodyAdmin(admin.ModelAdmin):
    list_display = ['title', 'footer', ]


# Обращение пользователя насчет багов
admin.site.register(Bug, BugAdmin)
admin.site.register(MailFooter, MailFooterAdmin)
admin.site.register(MailBody, MailBodyAdmin)
