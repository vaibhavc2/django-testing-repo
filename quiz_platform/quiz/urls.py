from django.urls import path

from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('<int:pk>/submit/', views.submit_answer, name='submit_answer'),
    path('<int:pk>/results/', views.quiz_results, name='quiz_results'),
]