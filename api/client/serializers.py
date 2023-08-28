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
    types = serializers.SerializerMethodField()

    class Meta:
        model = ServicesPackage
        fields = "__all__"

    @staticmethod
    def get_types(instance):
        spp_list = ServicesPackagePrice.objects.filter(services_package=instance)
        return ServicesPackagePriceDataSerializer(spp_list, many=True).data


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


class ServicesPackagePriceDataSerializer(serializers.ModelSerializer):
    period = serializers.SerializerMethodField()

    class Meta:
        model = ServicesPackagePrice
        fields = ['price', 'period', 'count_period']

    @staticmethod
    def get_period(instance):
        return instance.period.title


# ===========
# Бизнес запрос
# ===========
class BusinessRequestSerializer(serializers.ModelSerializer):
    services_package_price = ServicesPackagePriceSerializer(many=True)

    class Meta:
        model = BusinessRequest
        fields = "__all__"
