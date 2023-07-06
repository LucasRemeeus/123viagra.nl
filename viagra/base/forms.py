import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea

from .models import Medicine, Profile, Collection


class medicijnForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ("name", "manufacturer", "cures", "sideEffects")
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control"
            }),
            'manufacturer': TextInput(attrs={
                'class': "form-control"
            }),
            'cures': Textarea(attrs={
                'class': "form-control"
            }),
            'sideEffects': Textarea(attrs={
                'class': "form-control"
            })
        }


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bioText", "city", "dateOfBirth")
        widgets = {
            'bioText': Textarea(attrs={
                'class': "form-control"
            }),
            'city': TextInput(attrs={
                'class': "form-control"
            }),
            'dateOfBirth': forms.widgets.DateInput(attrs={
                'type': "date",
                'class': "form-control"
            })
        }


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ("medicine", "user", "date")
        widgets = {
            'date': forms.widgets.DateInput(attrs={
                'type': "date",
                'class': "form-control"
            })
        }
