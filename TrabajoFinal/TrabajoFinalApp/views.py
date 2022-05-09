from ast import Return
from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from TrabajoFinalApp.forms import ContactoForm
from django.http import HttpResponseRedirect
from .forms import CustomUserCreateForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required
def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')
@login_required
def contact(request):
    submitted = False
    if request.method=="POST":
        miformulario=ContactoForm(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            return HttpResponseRedirect('contact')

    else:
        miformulario=ContactoForm
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'contact.html', {'miformulario':miformulario, 'submitted': submitted} )


def inicio(request):
    return render(request, 'inicio.html')







def registro(request):
    data = {
        'form': CustomUserCreateForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreateForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)

            return redirect(to="inicio")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


