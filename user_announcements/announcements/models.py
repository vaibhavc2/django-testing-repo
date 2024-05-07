from django.contrib.auth.models import User
from django.db import models


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_topics = models.CharField(max_length=200)
    viewed_announcements = models.TextField()

    def __str__(self):
        return self.user.username


class Announcement(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.topic