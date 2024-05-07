from django.urls import path

from . import views

urlpatterns = [
    path('update_preferences/', views.update_preferences, name='update_preferences'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
]