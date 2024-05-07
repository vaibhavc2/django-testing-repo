from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_survey, name='create_survey'),
    path('success/', views.success, name='success'),
]