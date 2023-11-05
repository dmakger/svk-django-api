from rest_framework import serializers

from .models import Menu, Page, File


# ===========
# Файлы
# ===========
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["title", "file"]


# ===========
# Страница
# ===========
class PageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["path", "title"]


class PageSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = Page
        fields = ["path", "title", "description", "content", "files"]


# ===========
# Меню
# ===========
class MenuTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', "path", "title"]


class MenuSerializer(serializers.ModelSerializer):
    pages = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'title', 'path', 'pages']

    @staticmethod
    def get_pages(instance):
        page_list = Page.objects.filter(menu=instance, isVisible=True).order_by('number', 'title')
        return PageTitleSerializer(page_list, many=True).data
