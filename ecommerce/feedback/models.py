from django.db import models


class Feedback(models.Model):
    rating = models.IntegerField()
    comments = models.TextField()
    email = models.EmailField(blank=True)