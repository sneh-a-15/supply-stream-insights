from django import forms
from .models import UserPreference, CATEGORY_CHOICES

class PreferenceForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="Select your preferred categories"
    )

    class Meta:
        model = UserPreference
        fields = ['category']
        widgets = {
            'category': forms.Select(choices=CATEGORY_CHOICES)
        }
