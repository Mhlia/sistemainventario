from django.contrib import admin
from .models import Products, Pedido, Equipo
from django.contrib.auth.models import Group


admin.site.site_header = "DMZ Admin Dashboard" #Personalizacion el encabezado del sitio

class ProductsAdmin(admin.ModelAdmin): #Personalizacion del modelo Products
    list_display = ('nombre', 'marca', 'category')
    list_filter = ['category', 'marca']
    
  
class PedidoAdmin(admin.ModelAdmin): #Personalizacion del modelo Pedido
    list_display = ('producto', 'staff', 'cantidad_solicitada', 'fecha_solicitud')
    list_filter = ['staff',]

class EquipoAdmin(admin.ModelAdmin): #Personalizacion del modelo Equipo
    list_display = ('producto', 'serial')
    list_filter = ['producto',]

#Registro de los modelos con sus personalizaciones
admin.site.register(Products, ProductsAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Equipo, EquipoAdmin)
