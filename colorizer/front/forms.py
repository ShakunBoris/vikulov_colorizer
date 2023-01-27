from django.forms import ModelForm
from .models import *
class ApplicationForm(ModelForm):
    class Meta:
        model: Application