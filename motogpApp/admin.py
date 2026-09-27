from django.contrib import admin
from .models import Categoria, Escuderia, Piloto

# Registramos los modelos para que aparezcan en el panel web
admin.site.register(Categoria)
admin.site.register(Escuderia)
admin.site.register(Piloto)