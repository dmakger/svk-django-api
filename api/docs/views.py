from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Menu
from .serializers import MenuSerializer


# ===========
# Меню
# ===========
class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def get_toc(self, request):
        result = self.serializer_class(self.queryset, many=True).data
        return Response(result, status=status.HTTP_200_OK)
