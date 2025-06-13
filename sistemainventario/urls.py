"""
URL configuration for sistemainventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static 
# Configuración de las URLs del proyecto sistemainventario

urlpatterns = [
    path('admin/', admin.site.urls), # URL del panel de administración
    path('', include('dashboard.urls')), # URL de la aplicación dashboard
    path('register/', user_views.register, name='user-register'), # Registro de usuario
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'), # Login de usuario
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'), # Logout de usuario
    path('profile/', user_views.profile, name='user-profile'), # Perfil de usuario
    path('profile/update/', user_views.profile_update, name='user-profile-update'), # Actualizar perfil de usuario
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), # Vista para restablecer contraseña
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), # Vista de confirmación de restablecimiento de contraseña
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), # Vista para confirmar el restablecimiento de contraseña
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), # Vista de finalización del restablecimiento de contraseña
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # URL para servir archivos multimedia en modo de desarrollo