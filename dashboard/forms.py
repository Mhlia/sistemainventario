from django import forms
from .models import Products, Pedido, Equipo

class EquipmentForm(forms.ModelForm): # Formulario para el modelo Equipo
    class Meta:
        model = Equipo
        fields = ['producto', 'serial']

class ProductForm(forms.ModelForm): # Formulario para el modelo Products
    class Meta:
        model = Products
        fields = ['nombre', 'marca', 'category']


class OrderForm(forms.ModelForm): # Formulario para el modelo Pedido
    class Meta:
        model = Pedido
        fields = ['producto', 'cantidad_solicitada']
