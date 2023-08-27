from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientView
#                     BrandPartnerView, BrandPartnerDetailView, \
#                     ArticleView, ArticleDetailView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Клиент
    path("client/create/", ClientView.as_view({'post': 'create_client'})),
]
