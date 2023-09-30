from rest_framework import serializers
from bugs.models import Bug


# ===========
# Обращение пользователя насчет багов
# ===========
class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"
