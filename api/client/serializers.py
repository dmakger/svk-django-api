from rest_framework import serializers

from .models import SocialNetwork, Client, BusinessRequest, ServicesPackagePrice, ServicesPackage, Period


# ===========
# Соц сети пользователя
# ===========
class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = "__all__"


# ===========
# Клиент
# ===========
class ClientSerializer(serializers.ModelSerializer):
    communication = SocialNetworkSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__"


# ===========
# Пакеты услуг
# ===========
class ServicesPackageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPackage
        fields = ["title"]


class ServicesPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPackage
        fields = "__all__"


class PeriodTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ["title"]


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = "__all__"


class ServicesPackagePriceSerializer(serializers.ModelSerializer):
    services_package = ServicesPackageTitleSerializer()
    period = PeriodTitleSerializer()

    class Meta:
        model = ServicesPackagePrice
        fields = "__all__"


# ===========
# Бизнес запрос
# ===========
class BusinessRequestSerializer(serializers.ModelSerializer):
    services_package_price = ServicesPackagePriceSerializer(many=True)

    class Meta:
        model = BusinessRequest
        fields = "__all__"
