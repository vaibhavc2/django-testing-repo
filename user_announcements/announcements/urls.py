from announcements.views import user_announcements
from django.urls import path

urlpatterns = [
    path('announcements/<int:user_id>/', user_announcements, name='user_announcements'),
]