from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    category = models.CharField(max_length=100)
    publication_date = models.DateField()
    availability_status = models.BooleanField(default=True)
    borrower = models.CharField(max_length=100, blank=True, null=True)