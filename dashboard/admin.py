from django.contrib import admin
from .models import Products, Pedido
from django.contrib.auth.models import Group


admin.site.site_header = "DMZ Admin Dashboard"

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('serial', 'nombre', 'marca', 'category', 'cantidad')
    list_filter = ['category', 'marca']
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'staff', 'cantidad_solicitada', 'fecha_solicitud')
    list_filter = ['staff',]
    

admin.site.register(Products, ProductsAdmin)
admin.site.register(Pedido, PedidoAdmin)
# admin.site.unregister(Group) 
