from django.contrib import admin
from . import models
from .models import Category, Post, Comment



# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Comment)