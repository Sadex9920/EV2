from django.shortcuts import render

# Vista principal de MotoGP
def inicio(request):
    return render(request, 'motogp/inicio.html')

# Vista de la parrilla de pilotos
def pilotos(request):
    # Lista vacía temporal para evitar caídas
    context = {
        'pilotos': [] 
    }
    return render(request, 'motogp/pilotos.html', context)