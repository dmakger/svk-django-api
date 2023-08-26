from rest_framework import serializers

from .models import BrandPartner, Article, Tag, Writer


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
# Теги
# ===========
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("title",)


# ===========
# Писатели
# ===========
class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ("avatar_image", "lastname", "firstname", "pastname", )


# ===========
# Статьи
# ===========
class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = ("path", "title", "description", "preview_image", "time_at", "date_at", "tags")


class ArticleDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = ("path", "title", "description", "preview_image", "time_at", "date_at", "tags")

