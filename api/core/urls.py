from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BrandSupportView, \
                    BrandPartnerView, BrandPartnerDetailView, \
                    ArticleView, ArticleDetailView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Поддержка бренда
    path("brand_supports/", BrandSupportView.as_view({'get': 'get_brands'})),

    # Партнёры бренда
    path("brand_partners/", BrandPartnerView.as_view({'get': 'get_brands'})),
    path("brand_partners/<slug:path>/", BrandPartnerDetailView.as_view({'get': 'get_detail_brand_partner'})),

    # Статьи партнёра
    path("brand_partners/<slug:path>/article/", ArticleView.as_view({'get': 'get_articles'})),
    path("article/<slug:path>/", ArticleDetailView.as_view({'get': 'get_detail_article'})),
]
