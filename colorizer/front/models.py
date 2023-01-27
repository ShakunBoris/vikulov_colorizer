from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    pass

class Application(models.Model):
    class APPLICATION_STATUSES(models.IntegerChoices):
        PENDING = 0
        ANSWERED = 1
        DONE = 2
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    country = CountryField(blank_label='(select country)')
    whatsapp = PhoneNumberField(blank=True)
    status = models.IntegerField(choices=APPLICATION_STATUSES.choices, default=0)
    