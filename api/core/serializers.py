from rest_framework import serializers

from .models import BrandPartner, Article


# ===========
# Партнёры бренда
# ===========
class BrandPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPartner
        fields = ("path", "title", "logo_image")


class BrandPartnerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPartner
        fields = '__all__'


# ===========
# Статьи
# ===========
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("path", "title", "description", "preview_image", "time_at", "date_at", "tags")
