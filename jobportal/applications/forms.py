from django import forms

from .models import (AdditionalQualifications, EducationBackground,
                     PersonalInformation, WorkExperience)


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = '__all__'

class EducationBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationBackground
        fields = '__all__'

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class AdditionalQualificationsForm(forms.ModelForm):
    class Meta:
        model = AdditionalQualifications
        fields = '__all__'