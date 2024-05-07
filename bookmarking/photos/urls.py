from django.urls import path

from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
    path('remove_bookmark/', views.remove_bookmark, name='remove_bookmark'),
]