"""
URL configuration for evaluacion1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from core import views as core_views  # Importamos las vistas de recuperación de core
from evaluacion1 import views as global_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login_raiz'),
    path('home/', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    
    # Rutas Globales de Gestión de Usuarios
    path('usuarios/', global_views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', global_views.crear_usuario, name='crear_usuario'),
    
    # FLUJO DE RECUPERACIÓN DE CONTRASEÑA (EV3)
    path('recuperar/', core_views.solicitar_codigo, name='solicitar_codigo'),
    path('recuperar/verificar/', core_views.verificar_codigo, name='verificar_codigo'),
    path('recuperar/nueva-clave/', core_views.nueva_password, name='nueva_password'),
    
    path('ufc/', include('ufcApp.urls')),
    path('motogp/', include('motogpApp.urls')),
    path('cuentas/', include('django.contrib.auth.urls')),
]
