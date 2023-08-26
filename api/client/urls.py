from django.urls import path, include
from rest_framework.routers import DefaultRouter
#
# from .views import BrandSupportView, \
#                     BrandPartnerView, BrandPartnerDetailView, \
#                     ArticleView, ArticleDetailView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
