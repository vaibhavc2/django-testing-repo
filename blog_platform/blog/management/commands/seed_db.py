from blog.models import Comment, Post
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Seed database with random data'

    def handle(self, *args, **kwargs):
      # Check if the user exists
      user, created = User.objects.get_or_create(username='user1')
      
      # If the user was just created, set their password
      if created:
          user.set_password('password')
          user.save()

      # Create a post
      post = Post.objects.create(title='Post 1', content='Content 1', author=user)

      # Create a comment
      Comment.objects.create(content='Comment 1', author=user, post=post)

      self.stdout.write(self.style.SUCCESS('Database seeded!'))