from django.db import models
from django.contrib.auth.models import User

# Create your models here. 

class Perfil(models.Model): 
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=11, null=True, blank=True)
    imagen = models.ImageField(default='avatar.jpg', upload_to='perfil_imagenes', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return f'{self.staff.username} Perfil'
    