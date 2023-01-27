from django.forms import ModelForm
from .models import *
class ApplicationForm(ModelForm):
    class Meta:
        model =  Application
        fields = ['first_name', 'last_name', 'email', 'country', 'whatsapp']
        
