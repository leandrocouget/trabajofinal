from django.urls import path
from TrabajoFinalApp import views
from .forms import ContactoForm
from .views import registro, login

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('about', views.about, name="about"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('base', views.base, name="base"),
    path('registro', views.registro, name="registro"),
    path('login', views.login, name="login"),

]
