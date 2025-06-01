from django import forms
from .models import Products, Pedido, Equipo

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['producto', 'serial']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['nombre', 'marca', 'category']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto', 'cantidad_solicitada']
