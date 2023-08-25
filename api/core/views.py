from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BrandPartner, Article
from .serializers import BrandPartnerSerializer, BrandPartnerDetailSerializer, ArticleSerializer
from .service.error.error_view import BrandPartnerError
from .service.order import Order
from .service.paginator import Pagination
# from .service.params import params
from .service.splite import Splitting
from .service.validator import Validator


# ===========
# Партнеры бренда
# ===========
class BrandPartnerView(viewsets.ModelViewSet):
    serializer_class = BrandPartnerSerializer
    queryset = BrandPartner.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_brand_partners(self, request):
        qs = Order.by(self.queryset, request)
        result = Pagination(request=request, queryset=qs).get()
        serializer = self.serializer_class(result.get('results'), many=True)
        result['results'] = serializer.data
        return Response(result, status=status.HTTP_200_OK, )


class BrandPartnerDetailView(viewsets.ModelViewSet):
    serializer_class = BrandPartnerDetailSerializer
    queryset = BrandPartner.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = BrandPartnerError()

    @action(methods=['get'], detail=True)
    def get_detail_brand_partner(self, request, path):
        qs = self.queryset.filter(path=path)
        validator = Validator(qs, self.error_adapter)
        validator.full()
        if validator.has_error:
            return validator.error

        result = self.serializer_class(qs[0]).data
        return Response(result, status=status.HTTP_200_OK)


# ===========
# Статьи
# ===========
class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = BrandPartnerError()

    @action(methods=['get'], detail=False)
    def get_articles(self, request, **kwargs):
        qs = self.queryset.filter(brand__path=kwargs.get('path'))
        validator = Validator(qs, self.error_adapter)
        validator.full()
        if validator.has_error:
            return validator.error
        qs = Order.by(qs, request)
        result = Pagination(request=request, queryset=qs).get()
        serializer = self.serializer_class(instance=result.get('results'), many=True)
        result['results'] = serializer.data
        return Response(result, status=status.HTTP_200_OK)
    # return Splitting(self, request=request, qs=qs, serializer_body={'many': True}).complete()
