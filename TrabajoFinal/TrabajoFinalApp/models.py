import email
from urllib import request
from django.db import models



# Create your models here.

class contacto(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre +  ' ' + ' '+ self.email
    


