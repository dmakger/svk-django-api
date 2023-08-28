from rest_framework import serializers

from .models import Menu, Page


# ===========
# Страница
# ===========
class PageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["path", "title"]


# ===========
# Меню
# ===========
class MenuSerializer(serializers.ModelSerializer):
    pages = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = "__all__"

    @staticmethod
    def get_pages(instance):
        page_list = Page.objects.filter(menu=instance)
        return PageTitleSerializer(page_list, many=True).data