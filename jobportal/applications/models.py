from django.db import models


class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)

class EducationBackground(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField()

class AdditionalQualifications(models.Model):
    certification_name = models.CharField(max_length=200)
    certification_body = models.CharField(max_length=200)
    date_obtained = models.DateField()