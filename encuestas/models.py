from django.db import models

class Encuesta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    TIPO_TEXTO = 'texto'
    TIPO_UNA = 'una'
    TIPO_MULTIPLE = 'varias'
    TIPO_CHOICES = [
        (TIPO_TEXTO, 'Respuesta abierta'),
        (TIPO_UNA, 'Opción única'),
        (TIPO_MULTIPLE, 'Opción múltiple'),
    ]

    encuesta = models.ForeignKey(Encuesta, related_name='preguntas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default=TIPO_TEXTO)
    opciones = models.TextField(blank=True, help_text="Cada opción en una línea para preguntas de opción.")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'id']

    def opciones_list(self):
        return [o.strip() for o in self.opciones.splitlines() if o.strip()]

    def __str__(self):
        return f"{self.texto} ({self.get_tipo_display()})"

class Participante(models.Model):
    nombre = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre or f"Participante {self.id}"

class Respuesta(models.Model):
    participante = models.ForeignKey(Participante, related_name='respuestas', on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
    respuesta_texto = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"R:{self.pregunta.id} - P:{self.participante.id}"
