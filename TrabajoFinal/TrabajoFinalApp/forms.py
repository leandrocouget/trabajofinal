from dataclasses import field, fields
from django.forms import ModelForm
from django import forms
from .models import contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(ModelForm):
    class Meta:
        model = contacto
        fields = ('nombre', 'telefono', 'email', 'mensaje')
        
class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']