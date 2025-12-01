from django.db import models

class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    activa = models.BooleanField(default=True)

    class Meta:
        db_table = 'encuesta'
        managed = False

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    id_encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, db_column='id_encuesta')
    texto = models.CharField(max_length=255)

    class Meta:
        db_table = 'pregunta'
        managed = False

    def __str__(self):
        return self.texto


class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=150)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    id_encuesta_asignada = models.ForeignKey(
        Encuesta, on_delete=models.SET_NULL, null=True, db_column='id_encuesta_asignada', blank=True
    )

    class Meta:
        db_table = 'participante'
        managed = False

    def __str__(self):
        return self.username


class Respuesta(models.Model):
    OPCIONES = [
        ('Regular', 'Regular'),
        ('Bueno', 'Bueno'),
        ('Excelente', 'Excelente'),
        ('No Responde', 'No Responde'),
    ]

    id_respuesta = models.AutoField(primary_key=True)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, db_column='id_pregunta')
    id_participante = models.ForeignKey(Participante, on_delete=models.CASCADE, db_column='id_participante')
    valor = models.CharField(max_length=20, choices=OPCIONES)
    fecha_respuesta = models.DateTimeField()

    class Meta:
        db_table = 'respuesta'
        managed = False

    def __str__(self):
        return f"{self.id_participante} - {self.id_pregunta} - {self.valor}"
