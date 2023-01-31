from django.shortcuts import render
from django.urls import reverse
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'front/index.html', {})

def contact(request):
    if request.method =="POST":
        form = ApplicationForm(request.POST)
        if  form.is_valid():
            form.save()
            return render(request, 'front/contact.html', {
                'form': form,
                'success': 'true',
                })
        else:
            return render(request, 'front/contact.html', {
                'form': form,
                'success': 'false'
                })
    return render(request, 'front/contact.html', {
            'form': ApplicationForm()
            })