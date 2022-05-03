from django.urls import path
from TrabajoFinalApp import views

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('about', views.about, name="about"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('base', views.base, name="base"),
    path('blog', views.blog, name="blog"),

]
