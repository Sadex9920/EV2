from django import forms
from .models import Peleador, Combate

class PeleadorForm(forms.ModelForm):
    class Meta:
        model = Peleador
        fields = ['nombre', 'apodo', 'record', 'categoria', 'gimnasio', 'imagen_url']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: Islam Makhachev'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: The Eagle (Opcional)'}),
            'record': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: 26-1-0'}),
            'categoria': forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'gimnasio': forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'imagen_url': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'URL de imagen o ruta estática'}),
        }

    # Validación del formato de récord (Victorias-Derrotas-Empates)
    def clean_record(self):
        record = self.cleaned_data.get('record', '')
        partes = record.split('-')
        if len(partes) != 3 or not all(p.isdigit() for p in partes):
            raise forms.ValidationError("El récord debe tener el formato numérico V-D-E (ejemplo: 26-1-0).")
        return record


class CombateForm(forms.ModelForm):
    class Meta:
        model = Combate
        fields = ['evento', 'fecha', 'categoria', 'esquina_roja', 'esquina_azul', 'por_titulo']
        widgets = {
            'evento': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: UFC 310'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'esquina_roja': forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'esquina_azul': forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'por_titulo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Validaciones relacionales de la Transacción Operacional
    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        roja = cleaned_data.get('esquina_roja')
        azul = cleaned_data.get('esquina_azul')

        if roja and azul:
            if roja == azul:
                raise forms.ValidationError("Error de validación: Un peleador no puede enfrentarse a sí mismo.")
            if categoria:
                if roja.categoria != categoria or azul.categoria != categoria:
                    raise forms.ValidationError(
                        f"Error de validación: Ambos peleadores deben pertenecer a la categoría seleccionada ({categoria.nombre})."
                    )
        return cleaned_data