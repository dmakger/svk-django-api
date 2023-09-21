from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MenuView, PageView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Меню
    path("toc/", MenuView.as_view({'get': 'get_toc'})),

    # Страница
    path("page/<slug:path>/", PageView.as_view({'get': 'get_page'})),
]
