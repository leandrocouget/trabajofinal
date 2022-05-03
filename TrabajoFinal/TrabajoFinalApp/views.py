from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def inicio(request):
    return render(request, 'inicio.html')

def blog(request):
    return render(request, 'blog.html')

