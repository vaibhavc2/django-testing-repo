from django.core.management.base import BaseCommand
from photos.models import Photo


class Command(BaseCommand):
    help = 'Seeds the database with photos'

    def handle(self, *args, **options):
        Photo.objects.create(title='Example photo - 1', image='example1.jpg')
        Photo.objects.create(title='Example photo - 2', image='example2.jpg')
        self.stdout.write(self.style.SUCCESS('Successfully seeded database with photos'))