from announcements.models import Announcement, UserPreferences
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        fake = Faker()

        # Create a user
        user = User.objects.create_user(username='testuser', password='12345')

        # Create user preferences
        UserPreferences.objects.create(
            user=user,
            preferred_topics='topic1,topic2,topic3',
            viewed_announcements=''
        )

        # Create sample announcements
        for _ in range(50):
            Announcement.objects.create(
                topic=fake.word(ext_word_list=['topic1', 'topic2', 'topic3', 'topic4', 'topic5']),
                content=fake.text()
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))