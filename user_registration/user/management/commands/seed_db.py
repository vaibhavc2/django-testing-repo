from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from user.models import User


class Command(BaseCommand):
   
    def handle(self, *args, **kwargs):
        total = 3 # Number of users to be created
        for i in range(total):
            User.objects.create(username=get_random_string(10), email=f'user{i}@example.com')