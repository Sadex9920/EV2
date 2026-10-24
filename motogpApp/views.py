from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Piloto
from .forms import PilotoForm

@login_required
def inicio(request):
    return render(request, 'motogp/inicio.html')

@login_required
def pilotos(request):
    query = request.GET.get('q', '').strip()
    if query:
        lista_pilotos = Piloto.objects.filter(
            Q(nombre__icontains=query) |
            Q(numero__icontains=query) |
            Q(escuderia__nombre__icontains=query) |
            Q(categoria__nombre__icontains=query)
        )
    else:
        lista_pilotos = Piloto.objects.all()
        
    return render(request, 'motogp/pilotos.html', {'pilotos': lista_pilotos, 'query': query})

@login_required
def crear_piloto(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Piloto registrado correctamente.')
            return redirect('motogp_pilotos')
    else:
        form = PilotoForm()
    return render(request, 'motogp/piloto_form.html', {'form': form, 'accion': 'Agregar'})

@login_required
def editar_piloto(request, id):
    piloto = get_object_or_404(Piloto, id=id)
    if request.method == 'POST':
        form = PilotoForm(request.POST, instance=piloto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos del piloto actualizados.')
            return redirect('motogp_pilotos')
    else:
        form = PilotoForm(instance=piloto)
    return render(request, 'motogp/piloto_form.html', {'form': form, 'accion': 'Modificar', 'piloto': piloto})

@login_required
def eliminar_piloto(request, id):
    piloto = get_object_or_404(Piloto, id=id)
    if request.method == 'POST':
        piloto.delete()
        messages.success(request, 'Piloto eliminado de la parrilla.')
        return redirect('motogp_pilotos')
    return render(request, 'motogp/piloto_confirm_delete.html', {'piloto': piloto})