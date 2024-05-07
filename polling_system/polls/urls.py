from django.urls import path

from . import views

urlpatterns = [
    path('polls/<int:pk>/', views.poll_detail, name='poll_detail'),
]