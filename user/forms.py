from django import forms
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm): # Formulario para crear un nuevo usuario
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        
class UserUpdateForm(forms.ModelForm): # Formulario para actualizar la información del usuario
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class PerfilUpdateForm(forms.ModelForm): # Formulario para actualizar el perfil del usuario
    
    class Meta:
        model = Perfil
        fields = ['direccion', 'telefono', 'imagen']
        