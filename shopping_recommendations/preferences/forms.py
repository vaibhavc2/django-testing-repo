from django import forms

from .models import UserPreferences


class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['preferred_categories', 'viewed_products', 'purchased_items']