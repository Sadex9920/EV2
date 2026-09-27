from django.shortcuts import render
from .models import Piloto # Importamos tu nueva tabla

def pilotos(request):
    # Vamos a la base de datos y sacamos a todos los pilotos
    lista_pilotos = Piloto.objects.all()
    
    # Se los enviamos al HTML
    return render(request, 'motogp/pilotos.html', {'pilotos': lista_pilotos})