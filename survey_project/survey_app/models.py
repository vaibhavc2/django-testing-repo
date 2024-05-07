from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)