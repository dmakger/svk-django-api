from django.contrib import admin

from .models import BrandSupport, BrandPartner, Writer, Article, Tag

admin.site.register(BrandSupport)
admin.site.register(BrandPartner)
admin.site.register(Writer)
admin.site.register(Article)
admin.site.register(Tag)