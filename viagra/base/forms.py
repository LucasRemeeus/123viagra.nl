import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Medicine, Profile, Collection


class medicijnForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ("name", "manufacturer", "cures", "sideEffects")


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bioText", "city", "dateOfBirth")
        widgets = {
            'dateOfBirth': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ("medicine", "user")
