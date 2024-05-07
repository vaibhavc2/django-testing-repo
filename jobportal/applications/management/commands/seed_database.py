from applications.models import (AdditionalQualifications, EducationBackground,
                                 PersonalInformation, WorkExperience)
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
  help = 'Seeds the database with sample data'

  def handle(self, *args, **options):
        PersonalInformation.objects.create(first_name='John', last_name='Doe', email='john@example.com', phone_number='1234567890')
        EducationBackground.objects.create(school_name='XYZ University', degree='BSc Computer Science', field_of_study='Computer Science', start_date=timezone.now(), end_date=timezone.now())
        WorkExperience.objects.create(company_name='ABC Corp', job_title='Software Developer', start_date=timezone.now(), end_date=timezone.now(), job_description='Developing software')
        AdditionalQualifications.objects.create(certification_name='Certified Python Developer', certification_body='Python Institute', date_obtained=timezone.now())
