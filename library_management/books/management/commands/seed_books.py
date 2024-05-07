import random

from books.models import Book
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Seeds the database with random books'

    def handle(self, *args, **options):
        titles = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10']
        authors = ['Author1', 'Author2', 'Author3', 'Author4', 'Author5', 'Author6', 'Author7', 'Author8', 'Author9', 'Author10']
        categories = ['Category1', 'Category2', 'Category3', 'Category4', 'Category5']

        for i in range(10):
            Book.objects.create(
                title=random.choice(titles),
                author=random.choice(authors),
                isbn=''.join(random.choices('1234567890', k=13)),
                category=random.choice(categories),
                publication_date=timezone.now(),
                availability_status=True
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with random books'))