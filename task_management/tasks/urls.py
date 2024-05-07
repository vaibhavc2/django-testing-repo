from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/complete/<int:pk>/', views.complete_task, name='complete_task'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.create_task, name='create_task'),
]