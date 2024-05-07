from django.shortcuts import render

from .forms import (AdditionalQualificationsForm, EducationBackgroundForm,
                    PersonalInformationForm, WorkExperienceForm)


def personal_information(request):
    form = PersonalInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'personal_information.html', {'form': form})

def education_background(request):
    form = EducationBackgroundForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'education_background.html', {'form': form})

def work_experience(request):
    form = WorkExperienceForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'work_experience.html', {'form': form})

def additional_qualifications(request):
    form = AdditionalQualificationsForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'additional_qualifications.html', {'form': form})