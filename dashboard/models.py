from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Monitor', 'Monitor'),
    ('Laptop', 'Laptop'),
    ('Escritorio', 'Escritorio'),
    ('Servidor', 'Servidor'),
)

MARCAS = (
    ('HP', 'HP'),
    ('Dell', 'Dell'),
    ('Lenovo', 'Lenovo'),
    ('Asus', 'Asus'),
    ('Acer', 'Acer'),
    ('Apple', 'Apple'),
)


class Products(models.Model):
    serial = models.CharField(max_length=20, unique=True, blank=True, null=True) 
    nombre = models.CharField(max_length=15, null=True, blank=True)
    marca = models.CharField(max_length=10, choices=MARCAS, null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY, null=True, blank=True)
    cantidad = models.PositiveIntegerField(null=True, blank=True) 
    
    
    
    class Meta:
        verbose_name_plural = 'Productos'
       
    def __str__(self):
        return f'{self.nombre} - {self.cantidad}'

class Pedido(models.Model):
    producto = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    cantidad_solicitada = models.PositiveIntegerField(null=True, blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.producto} pedido por {self.staff.username}'
