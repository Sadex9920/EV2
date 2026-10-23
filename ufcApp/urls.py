from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='ufc_inicio'),
    path('equipo/', views.peleadores, name='ufc_peleadores'),
    path('equipo/agregar/', views.crear_peleador, name='crear_peleador'),
    path('equipo/editar/<int:id>/', views.editar_peleador, name='editar_peleador'),
    path('equipo/eliminar/<int:id>/', views.eliminar_peleador, name='eliminar_peleador'),
    path('combates/', views.combates, name='combates'),
    path('combates/eliminar/<int:id>/', views.eliminar_combate, name='eliminar_combate'),
]