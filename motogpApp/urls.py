from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='motogp_inicio'),
    path('pilotos/', views.pilotos, name='motogp_pilotos'),
    path('pilotos/agregar/', views.crear_piloto, name='crear_piloto'),
    path('pilotos/editar/<int:id>/', views.editar_piloto, name='editar_piloto'),
    path('pilotos/eliminar/<int:id>/', views.eliminar_piloto, name='eliminar_piloto'),
]