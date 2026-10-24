from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Peleador, Combate
from .forms import PeleadorForm, CombateForm

@login_required
def inicio(request):
    return render(request, 'ufc/inicio.html')

@login_required
def peleadores(request):
    query = request.GET.get('q', '').strip()
    if query:
        lista_peleadores = Peleador.objects.filter(
            Q(nombre__icontains=query) |
            Q(apodo__icontains=query) |
            Q(categoria__nombre__icontains=query) |
            Q(gimnasio__nombre__icontains=query)
        )
    else:
        lista_peleadores = Peleador.objects.all()
    
    context = {
        'peleadores': lista_peleadores,
        'query': query
    }
    return render(request, 'ufc/peleadores.html', context)

@login_required
def crear_peleador(request):
    if request.method == 'POST':
        form = PeleadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peleador registrado correctamente.')
            return redirect('ufc_peleadores')
    else:
        form = PeleadorForm()
    return render(request, 'ufc/peleador_form.html', {'form': form, 'accion': 'Agregar'})

@login_required
def editar_peleador(request, id):
    peleador = get_object_or_404(Peleador, id=id)
    if request.method == 'POST':
        form = PeleadorForm(request.POST, instance=peleador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos del peleador actualizados.')
            return redirect('ufc_peleadores')
    else:
        form = PeleadorForm(instance=peleador)
    return render(request, 'ufc/peleador_form.html', {'form': form, 'accion': 'Modificar', 'peleador': peleador})

@login_required
def eliminar_peleador(request, id):
    peleador = get_object_or_404(Peleador, id=id)
    if request.method == 'POST':
        peleador.delete()
        messages.success(request, 'Peleador eliminado del registro.')
        return redirect('ufc_peleadores')
    return render(request, 'ufc/peleador_confirm_delete.html', {'peleador': peleador})

@login_required
def combates(request):
    lista_combates = Combate.objects.select_related('categoria', 'esquina_roja', 'esquina_azul').all().order_by('-fecha')
    if request.method == 'POST':
        form = CombateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Combate oficial programado con éxito.')
            return redirect('combates')
    else:
        form = CombateForm()
    
    return render(request, 'ufc/combates.html', {'combates': lista_combates, 'form': form})

@login_required
def eliminar_combate(request, id):
    combate = get_object_or_404(Combate, id=id)
    if request.method == 'POST':
        combate.delete()
        messages.success(request, 'Combate cancelado y eliminado.')
    return redirect('combates')