from django import forms
from .models import Encuesta, Pregunta, Participante

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['titulo', 'descripcion']

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto', 'tipo', 'opciones', 'orden']

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre', 'email']
