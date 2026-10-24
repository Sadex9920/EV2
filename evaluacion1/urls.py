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
from django.contrib.auth.decorators import login_required  # Importamos el candado

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Bloqueamos la página de bienvenida desde la raíz
    path('', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    
    # Rutas de las aplicaciones
    path('ufc/', include('ufcApp.urls')),
    path('motogp/', include('motogpApp.urls')),
    
    # Rutas del Sistema de Autenticación de Django
    path('cuentas/', include('django.contrib.auth.urls')),
]
