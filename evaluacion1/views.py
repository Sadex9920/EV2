from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group

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

def editar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    grupos = Group.objects.all()
    
    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name', '')
        usuario.last_name = request.POST.get('last_name', '')
        usuario.email = request.POST.get('email', '')
        
        # Actualizar el grupo (perfil)
        grupo_id = request.POST.get('grupo')
        if grupo_id:
            usuario.groups.clear() # Limpiar grupos anteriores
            grupo = Group.objects.get(id=grupo_id)
            usuario.groups.add(grupo)
            
        usuario.save()
        messages.success(request, f"Usuario {usuario.username} actualizado correctamente.")
        return redirect('listar_usuarios')
        
    # Obtener el grupo actual del usuario para marcarlo en el select
    grupo_actual = usuario.groups.first()
    
    return render(request, 'usuarios/editar_usuario.html', {
        'usuario_edit': usuario,
        'grupos': grupos,
        'grupo_actual': grupo_actual
    })

def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        # Evitar que el superusuario se elimine a sí mismo
        if usuario.is_superuser and request.user == usuario:
            messages.error(request, "No puedes eliminar tu propia cuenta de Superusuario.")
        else:
            usuario.delete()
            messages.success(request, "Usuario eliminado del sistema.")
    return redirect('listar_usuarios')