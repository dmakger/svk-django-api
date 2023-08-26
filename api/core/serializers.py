from rest_framework import serializers

from .models import BrandPartner, Article, Tag, Writer, BrandSupport


# ===========
# Партнёры бренда
# ===========
class BrandSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandSupport
        fields = "__all__"


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
        fields = ("avatar_image", "lastname", "firstname", "pastname", "rank")


# ===========
# Статьи
# ===========
class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = ("path", "title", "description", "preview_image", "time_at", "date_at", "tags")


class ArticleDetailSerializer(serializers.ModelSerializer):
    brand = BrandPartnerSerializer()
    tags = TagSerializer(many=True)
    writer = WriterSerializer()

    class Meta:
        model = Article
        fields = ("path", "title", "writer", "brand", "description", "preview_image", "date_at", "content", "tags")
