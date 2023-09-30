from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bugs.views import BugView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Баги
    path("bug/create/", BugView.as_view({'post': 'create_bug'})),
]
