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
        fields = ["path", "title"]


class MenuSerializer(serializers.ModelSerializer):
    pages = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = "__all__"

    @staticmethod
    def get_pages(instance):
        page_list = Page.objects.filter(menu=instance)
        return PageTitleSerializer(page_list, many=True).data
