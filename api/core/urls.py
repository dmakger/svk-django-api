from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BrandPartnerView, BrandPartnerDetailView, \
                    ArticleView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Партнёры бренда
    path("brand_partners/", BrandPartnerView.as_view({'get': 'get_brand_partners'})),
    path("brand_partners/<slug:path>/", BrandPartnerDetailView.as_view({'get': 'get_detail_brand_partner'})),

    # Статьи партнёра
    path("brand_partners/<slug:path>/article/", ArticleView.as_view({'get': 'get_articles'})),
    path("article/<slug:path>/", ArticleView.as_view({'get': 'get_detail_article'})),
]
