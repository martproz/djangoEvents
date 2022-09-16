from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Venue

#venue Form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'adress', 'zip_code', 'phone', 'web', 'email_adress')

#1) Creo class en forms
#2) Creo html add_venue usando la plantilla de home
#3) Creo el path en urls.py
#4) Creo views.py
#5) Necesito crear un link en la navbar