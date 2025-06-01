from django.contrib import admin
from .models import Products, Pedido, Equipo
from django.contrib.auth.models import Group


admin.site.site_header = "DMZ Admin Dashboard"

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'category')
    list_filter = ['category', 'marca']
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'staff', 'cantidad_solicitada', 'fecha_solicitud')
    list_filter = ['staff',]

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'serial')
    list_filter = ['producto',]

admin.site.register(Products, ProductsAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Equipo, EquipoAdmin)
