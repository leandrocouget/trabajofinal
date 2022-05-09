from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from .models import Category, Post,Comment



# Create your views here.
@login_required
def blog(request):
    articulos = Post.objects.all()
    return render(request, 'blog.html', {"articulos":articulos})

