from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Definición de las categorías y marcas de productos
CATEGORY = (
    ('Monitor', 'Monitor'),
    ('Laptop', 'Laptop'),
    ('Escritorio', 'Escritorio'),
    ('Servidor', 'Servidor'),
)

# Definición de las marcas de productos
MARCAS = (
    ('HP', 'HP'),
    ('Dell', 'Dell'),
    ('Lenovo', 'Lenovo'),
    ('Asus', 'Asus'),
    ('Acer', 'Acer'),
    ('Apple', 'Apple'),
)

# Modelo de Productos
class Products(models.Model): # Modelo para almacenar información de productos
    nombre = models.CharField(max_length=100, null=True, blank=True)
    marca = models.CharField(max_length=50, choices=MARCAS, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Productos'
       
    def __str__(self): # Método para representar el modelo Products como una cadena
        return f'{self.nombre} - {self.marca}'
    
class Equipo(models.Model): # Modelo para almacenar información de equipos
    producto = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    serial = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.serial}' # Representación del modelo Equipo como una cadena

class Pedido(models.Model): # Modelo para almacenar información de pedidos
    producto = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    cantidad_solicitada = models.PositiveIntegerField(null=True, blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.producto} pedido por {self.staff.username}' # Representación del modelo Pedido como una cadena
