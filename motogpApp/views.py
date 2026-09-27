from django.shortcuts import render
from .models import Piloto

# Vista de la página principal de MotoGP
def inicio(request):
    return render(request, 'motogp/index.html')

# Vista de la grilla de pilotos que conectamos a la Base de Datos
def pilotos(request):
    lista_pilotos = Piloto.objects.all()
    return render(request, 'motogp/pilotos.html', {'pilotos': lista_pilotos})