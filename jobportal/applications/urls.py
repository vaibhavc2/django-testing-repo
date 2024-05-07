from django.urls import path

from . import views

urlpatterns = [
    path('personal_information/', views.personal_information, name='personal_information'),
    path('education_background/', views.education_background, name='education_background'),
    path('work_experience/', views.work_experience, name='work_experience'),
    path('additional_qualifications/', views.additional_qualifications, name='additional_qualifications'),
]