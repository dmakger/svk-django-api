from rest_framework import serializers

from .models import SocialNetwork, Client


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
