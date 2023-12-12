from django.contrib import admin

from .models import BrandSupport, BrandPartner, Writer, Article, Tag


class BrandSupportAdmin(admin.ModelAdmin):
    list_display = ['title', 'path', 'link', 'logo_image', 'number']


class BrandPartnerAdmin(admin.ModelAdmin):
    list_display = ['title', 'path', 'link', 'logo_image']


class WriterAdmin(admin.ModelAdmin):
    list_display = ['path', 'firstname', 'lastname', 'pastname', 'rank', 'description', 'avatar_image',
                    'number_articles']


class TagAdmin(admin.ModelAdmin):
    list_display = ['path', 'title', 'description']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'writer', 'path', 'date_at', 'formatted_tags']

    def formatted_tags(self, obj):
        return ', '.join(tag.title for tag in obj.tags.all())

    formatted_tags.short_description = 'Tags'


admin.site.register(BrandSupport, BrandSupportAdmin)
admin.site.register(BrandPartner, BrandPartnerAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
