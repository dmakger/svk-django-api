from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Menu, Page
from .serializers import MenuSerializer, PageSerializer
from .service.error.error_view import PageError
from .service.validator.validator import Validator


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


# ===========
# Страница
# ===========
class PageView(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = PageError()

    @action(detail=False, methods=['get'])
    def get_page(self, request, path):
        qs = self.queryset.filter(path=path)
        validator = Validator(queryset=qs, error_adapter=self.error_adapter)
        validator.full()
        if validator.has_error:
            return validator.error

        result = self.serializer_class(qs[0]).data
        return Response(result, status=status.HTTP_200_OK)
