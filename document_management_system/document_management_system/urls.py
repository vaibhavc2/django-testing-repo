# document_management_system/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('file_management.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
