from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/core/v1/", include('core.urls')),
    path("api/client/v1/", include('client.urls')),
    path("api/docs/v1/", include('docs.urls')),
    path("api/bugs/v1/", include('bugs.urls')),
    path("ckeditor/", include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
