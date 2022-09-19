from django import forms
from django.forms import ModelForm
from .models import Venue, Event 

class EventForm(ModelForm): 
    class Meta:
        model = Event 
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'})
        }

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

