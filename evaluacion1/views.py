from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm

@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

@login_required
def crear_usuario(request):
    # Generamos los 3 perfiles exigidos por la rúbrica si no existen en la BD
    Group.objects.get_or_create(name='Administrador')
    Group.objects.get_or_create(name='Supervisor')
    Group.objects.get_or_create(name='Administrativo')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            grupo = form.cleaned_data.get('perfil')
            usuario.groups.add(grupo)
            messages.success(request, f'Usuario {usuario.username} creado con el perfil: {grupo.name}.')
            return redirect('listar_usuarios')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'usuarios/crear_usuario.html', {'form': form})