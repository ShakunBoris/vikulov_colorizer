from django.shortcuts import render
from django.urls import reverse
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'front/index.html', {})
