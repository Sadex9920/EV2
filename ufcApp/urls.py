from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='ufc_inicio'),
    path('equipo/', views.peleadores, name='ufc_peleadores'),
]