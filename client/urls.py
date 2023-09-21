from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientView, BusinessRequestView, ServicesPackageView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Клиент
    path("client/create/", ClientView.as_view({'post': 'create_client'})),

    # Запрос клиента
    path("business-request/create/", BusinessRequestView.as_view({'post': 'create_business_request'})),

    # Пакет услуг
    path("services-package/", ServicesPackageView.as_view({'get': 'get_services_package'})),
]
