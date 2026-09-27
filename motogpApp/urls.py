from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='motogp_inicio'),
    path('pilotos/', views.pilotos, name='motogp_pilotos'),
]