from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST) # Formulario de registro
        if form.is_valid(): 
            form.save() 
            return redirect('user-login') 
    else:
        form = CreateUserForm()
        
    context = {
        'form': form,
    }
    
    return render(request, 'user/register.html', context) # Formulario de registro

def login(request):
    return render(request, 'user/login.html') # Login de usuario

def logout(request):
    return render(request, 'user/logout.html') # Logout de usuario

def profile(request):
    return render(request, 'user/profile.html') # Perfil de usuario

def profile_update(request):
    context = {
        
    }
    return render(request, 'user/profile_update.html', context) # Actualizar perfil de usuario
