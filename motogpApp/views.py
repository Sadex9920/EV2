from django.shortcuts import render
from .models import Piloto

# Vista de la página principal de MotoGP apuntando a tu archivo
def inicio(request):
    return render(request, 'motogp/inicio.html')

# Vista de la grilla de pilotos
def pilotos(request):
    lista_pilotos = Piloto.objects.all()
    return render(request, 'motogp/pilotos.html', {'pilotos': lista_pilotos})