from django.core.management.base import BaseCommand
from encuestas.models import Encuesta, Pregunta

class Command(BaseCommand):
    help = 'Crear datos de ejemplo para encuestas rápidas'

    def handle(self, *args, **kwargs):
        e = Encuesta.objects.create(titulo='Satisfacción - Tienda Demo', descripcion='Encuesta rápida post-compra')
        Pregunta.objects.create(encuesta=e, texto='¿Cómo calificaría su experiencia?', tipo='una', opciones='Excelente\nBueno\nRegular\nMalo', orden=1)
        Pregunta.objects.create(encuesta=e, texto='¿Qué le gustó más?', tipo='texto', opciones='', orden=2)
        Pregunta.objects.create(encuesta=e, texto='¿Qué canales usó?', tipo='varias', opciones='Tienda física\nWeb\nApp\nTeléfono', orden=3)
        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados.'))
