from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from .models import Announcement, UserPreferences


def user_announcements(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_preferences = UserPreferences.objects.get(user=user)
    preferred_topics = user_preferences.preferred_topics.split(',')
    announcements = Announcement.objects.filter(topic__in=preferred_topics)
    return render(request, 'announcements.html', {'announcements': announcements})