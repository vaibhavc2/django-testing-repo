from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_uploads, name='list_uploads'),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
]
