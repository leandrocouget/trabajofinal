from ast import Return
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from TrabajoFinalApp.forms import FormularioContacto
from django.core.mail import send_mail


# Create your views here.

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method=="POST":
        miformulario=FormularioContacto(request.POST)

        if miformulario.is_valid():
            infForm = miformulario.cleaned_data

            send_mail(infForm['Nombre'], infForm['Mensaje'], infForm.get('email', ''),['leandrocouget@gmail.com'],)

            return render(request," Gracias.html")

    else:
        miformulario=FormularioContacto()

    return render(request, "formulario_contacto.html", {"form":miformulario} )



def inicio(request):
    return render(request, 'inicio.html')

def blog(request):
    return render(request, 'blog.html')

