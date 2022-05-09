from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    

    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = 'published')
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1 )
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    postobjects = PostObjects()
    
    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title
            
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="coments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ("publish",)
        
        def __str__(self):
            return f"Coment by  {self.name}"
        