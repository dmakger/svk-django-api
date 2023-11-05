from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BrandPartner, Article, BrandSupport
from .serializers import BrandPartnerSerializer, BrandPartnerDetailSerializer, ArticleSerializer, \
    ArticleDetailSerializer, BrandSupportSerializer
from .service.error.error_view import ArticleError, BrandPartnerError

from .service.order import Order
from .service.paginator import Pagination
from .service.splite import Splitting


# ===========
# Поддержка бренда
# ===========
class BrandSupportView(viewsets.ModelViewSet):
    serializer_class = BrandSupportSerializer
    queryset = BrandSupport.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_brands(self, request):
        qs = Order.by(self.queryset, request).order_by('number')
        result = Pagination(request=request, queryset=qs).get()
        serializer = self.serializer_class(result.get('results'), many=True)
        result['results'] = serializer.data
        return Response(result, status=status.HTTP_200_OK)


# ===========
# Партнеры бренда
# ===========
class BrandPartnerView(viewsets.ModelViewSet):
    serializer_class = BrandPartnerSerializer
    queryset = BrandPartner.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = BrandPartnerError()

    @action(methods=['get'], detail=False)
    def get_brands(self, request):
        qs = Order.by(self.queryset, request)
        result = Pagination(request=request, queryset=qs).get()
        serializer = self.serializer_class(result.get('results'), many=True)
        result['results'] = serializer.data
        return Response(result, status=status.HTTP_200_OK)


class BrandPartnerDetailView(viewsets.ModelViewSet):
    serializer_class = BrandPartnerDetailSerializer
    queryset = BrandPartner.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = BrandPartnerError()

    @action(methods=['get'], detail=True)
    def get_detail_brand_partner(self, request, path):
        qs = self.queryset.filter(path=path)
        return Splitting(
            self, request=request, qs=qs, serializer_body={'instance': qs[0]}
        ).complete(check_order=False, check_paginate=False)


# ===========
# Статьи
# ===========
class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = ArticleError()

    @action(methods=['get'], detail=False)
    def get_articles(self, request, **kwargs):
        qs = self.queryset.filter(brand__path=kwargs.get('path'))
        return Splitting(
            self, request=request, qs=qs, serializer_body={'many': True}
        ).complete()


class ArticleDetailView(viewsets.ModelViewSet):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = ArticleError()

    @action(methods=['get'], detail=True)
    def get_detail_article(self, request, path, **kwargs):
        qs = self.queryset.filter(path=path)
        return Splitting(
            self, request=request, qs=qs
        ).complete(check_order=False, check_paginate=False, my_qs=True, many=False)
