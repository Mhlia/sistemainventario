from django import forms
from .models import Products, Pedido

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['serial', 'nombre', 'marca', 'category', 'cantidad']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto', 'cantidad_solicitada']
