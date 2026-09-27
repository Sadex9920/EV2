from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Escuderia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField(help_text="Número del dorsal")
    edad = models.IntegerField()
    # Especificamos en el help_text tu regla de solo títulos de la categoría reina
    titulos = models.IntegerField(default=0, help_text="Solo campeonatos de MotoGP (no Moto2 ni Moto3)")
    imagen_url = models.CharField(max_length=500, blank=True, null=True, help_text="Link de internet o nombre de archivo local")
    
    # Llaves foráneas (Relaciones)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    escuderia = models.ForeignKey(Escuderia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"#{self.numero} - {self.nombre}"