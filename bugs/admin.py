from django.contrib import admin
from bugs.models import Bug, MailBody, MailFooter

# Обращение пользователя насчет багов
admin.site.register(Bug)
admin.site.register(MailBody)
admin.site.register(MailFooter)
