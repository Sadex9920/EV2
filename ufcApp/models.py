from django.db import models

# Tabla 1: Categorías de peso (Ej. Peso Ligero, Peso Welter)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Tabla 2: Gimnasios o equipos de entrenamiento (Ej. AKA)
class Gimnasio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

# Tabla 3: Luchadores (Entidad principal con relaciones Foráneas)
class Peleador(models.Model):
    nombre = models.CharField(max_length=100)
    apodo = models.CharField(max_length=100, blank=True, null=True)
    record = models.CharField(max_length=20) # Ejemplo: 22-0-0
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    gimnasio = models.ForeignKey(Gimnasio, on_delete=models.SET_NULL, null=True, blank=True)
    imagen_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.record})"