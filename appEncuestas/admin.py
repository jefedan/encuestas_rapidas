from django.contrib import admin
from .models import Encuesta, Pregunta, Respuesta, Participante

class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 1
    fields = ('texto','tipo','orden')

class EncuestaAdmin(admin.ModelAdmin):
    inlines = [PreguntaInline]
    list_display = ('titulo', 'fecha_creacion', 'preguntas_count')
    search_fields = ('titulo','descripcion')
    list_filter = ('fecha_creacion',)
    readonly_fields = ('fecha_creacion',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('preguntas')

    def preguntas_count(self, obj):
        return obj.preguntas.count()
    preguntas_count.short_description = 'N° preguntas'

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta','participante','fecha')
    search_fields = ('respuesta_texto',)
    list_filter = ('fecha',)
    readonly_fields = ('fecha',)

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Pregunta)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Participante)
