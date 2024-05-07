from django.core.management.base import BaseCommand
from preferences.models import Product


class Command(BaseCommand):
  help = 'Seeds the database with dummy data'

  def handle(self, *args, **options):
    # List of product names, descriptions, prices, and categories
    products = [
      ('Product 1', 'Description 1', 9.99, 'Category 1'),
      ('Product 2', 'Description 2', 19.99, 'Category 2'),
      ('Product 3', 'Description 3', 29.99, 'Category 1'),
      ('Product 4', 'Description 4', 39.99, 'Category 2'),
      ('Product 5', 'Description 5', 49.99, 'Category 1'),
      ('Product 6', 'Description 6', 59.99, 'Category 2'),
      ('Product 7', 'Description 7', 69.99, 'Category 1'),
      ('Product 8', 'Description 8', 79.99, 'Category 2'),
      ('Product 9', 'Description 9', 89.99, 'Category 1'),
      ('Product 10', 'Description 10', 99.99, 'Category 2'),
    ]

    # Create and save Product instances
    for name, description, price, category in products:
      Product.objects.create(name=name, description=description, price=price, category=category)

    self.stdout.write(self.style.SUCCESS('Database seeded!'))