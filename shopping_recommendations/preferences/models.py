from django.contrib.auth.models import User
from django.db import models


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_categories = models.TextField()
    viewed_products = models.TextField()
    purchased_items = models.TextField()


class Product(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  category = models.CharField(max_length=200)

  def __str__(self):
    return self.name