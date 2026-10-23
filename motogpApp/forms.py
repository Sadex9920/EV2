from django import forms
from .models import Piloto

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre', 'numero', 'edad', 'titulos', 'categoria', 'escuderia', 'imagen_url']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: Francesco Bagnaia'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: 1'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: 27'}),
            'titulos': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'min': 0}),
            'categoria': forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'escuderia': forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'imagen_url': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'URL de imagen o ruta estática'}),
        }

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if numero is not None and (numero < 1 or numero > 99):
            raise forms.ValidationError("El dorsal del piloto debe estar entre 1 y 99.")
        return numero

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad is not None and edad < 18:
            raise forms.ValidationError("El piloto debe tener al menos 18 años para competir en la categoría.")
        return edad