from django.core.management.base import BaseCommand
from tasks.models import Task


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        Task.objects.create(title='Task 1', description='This is task 1', completed=False)
        Task.objects.create(title='Task 2', description='This is task 2', completed=True)
        self.stdout.write(self.style.SUCCESS('Database seeded!'))
