from django.shortcuts import render
from .models import Peleador # Importamos la tabla de peleadores

def inicio(request):
    return render(request, 'ufc/inicio.html')

def peleadores(request):
    # El ORM extrae todos los registros de la base de datos
    lista_peleadores = Peleador.objects.all()
    
    context = {
        'peleadores': lista_peleadores 
    }
    return render(request, 'ufc/peleadores.html', context)