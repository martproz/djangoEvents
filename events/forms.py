from django import forms
from django.forms import ModelForm
from .models import Venue

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'adress', 'zip_code', 'phone', 'web', 'email_adress')
        labels = {
            'name': '',
            'adress': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_adress': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'adress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adress'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web'}),
            'email_adress': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }

