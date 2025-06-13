from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, PerfilUpdateForm
from django.contrib import messages

# Create your views here.

def register(request): # Vista para registrar un nuevo usuario
    if request.method == 'POST':
        form = CreateUserForm(request.POST) # Formulario de registro
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Se ha creado la cuenta para {username} correctamente. Por favor inicie sesion') # Mensaje de éxito
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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # Formulario de actualización de usuario
        perfil_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil) # Formulario de actualización de perfil
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('user-profile') # Redirigir a la vista de perfil después de actualizar
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilUpdateForm(instance=request.user.perfil)
    
    context = {
        'user_form': user_form,
        'perfil_form': perfil_form,
    }
    return render(request, 'user/profile_update.html', context) # Actualizar perfil de usuario
