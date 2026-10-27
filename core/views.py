from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
import random

# PASO 1: Solicitar correo y generar código
def solicitar_codigo(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Generar código de 5 dígitos
            codigo = str(random.randint(10000, 99999))
            
            # Guardar datos temporalmente en la sesión del navegador
            request.session['reset_email'] = email
            request.session['reset_code'] = codigo
            
            # Simular envío de correo (saldrá en la terminal por la configuración)
            send_mail(
                'Código de Recuperación - SportCenter',
                f'Hola {user.username}, tu código de recuperación de 5 dígitos es: {codigo}',
                'soporte@sportcenter.cl',
                [email],
                fail_silently=False,
            )
            return redirect('verificar_codigo')
            
        except User.DoesNotExist:
            messages.error(request, "No existe ninguna cuenta registrada con este correo electrónico.")
            
    return render(request, 'recuperacion/solicitar_codigo.html')

# PASO 2: Ingresar y validar el código de 5 dígitos
def verificar_codigo(request):
    # Si entra aquí sin haber puesto el correo antes, lo devolvemos al inicio
    if 'reset_email' not in request.session:
        return redirect('solicitar_codigo')
        
    if request.method == 'POST':
        codigo_ingresado = request.POST.get('codigo')
        codigo_real = request.session.get('reset_code')
        
        if codigo_ingresado == codigo_real:
            request.session['codigo_verificado'] = True
            return redirect('nueva_password')
        else:
            messages.error(request, "El código es incorrecto. Inténtalo nuevamente.")
            
    return render(request, 'recuperacion/verificar_codigo.html')

# PASO 3: Crear la nueva contraseña
def nueva_password(request):
    # Si no ha verificado el código, no puede entrar aquí
    if not request.session.get('codigo_verificado'):
        return redirect('solicitar_codigo')
        
    if request.method == 'POST':
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if pass1 == pass2:
            email = request.session.get('reset_email')
            user = User.objects.get(email=email)
            
            # Encriptar y guardar la nueva contraseña
            user.set_password(pass1)
            user.save()
            
            # Limpiar la sesión por seguridad
            del request.session['reset_email']
            del request.session['reset_code']
            del request.session['codigo_verificado']
            
            messages.success(request, "¡Tu contraseña ha sido actualizada exitosamente! Ya puedes iniciar sesión.")
            return redirect('login_raiz')
        else:
            messages.error(request, "Las contraseñas no coinciden. Inténtalo de nuevo.")
            
    return render(request, 'recuperacion/nueva_password.html')