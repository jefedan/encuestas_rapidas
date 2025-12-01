from django import forms
from .models import Encuesta, Pregunta, Participante

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'descripcion', 'activa']


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['id_encuesta', 'texto']


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre', 'correo', 'username', 'password', 'id_encuesta_asignada']


class ResponderEncuestaForm(forms.Form):
    OPCIONES = [
        ('Regular', 'Regular'),
        ('Bueno', 'Bueno'),
        ('Excelente', 'Excelente'),
        ('No Responde', 'No Responde'),
    ]
