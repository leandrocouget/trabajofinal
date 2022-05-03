import django


from django import forms

class FormularioContacto(forms.Form):
    Nombre = forms.CharField()
    Telefono = forms.CharField()
    Email = forms.EmailField()
    Mensaje = forms.CharField()
