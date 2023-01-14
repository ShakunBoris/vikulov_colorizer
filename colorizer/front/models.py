from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Create your models here.
class User(AbstractUser):
    pass

class Application(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    country = CountryField(blank_label='(select country)')
    # whatsapp
    # status 