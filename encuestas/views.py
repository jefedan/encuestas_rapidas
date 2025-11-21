from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Encuesta, Pregunta, Respuesta, Participante
from .forms import EncuestaForm, ParticipanteForm

class EncuestaListView(ListView):
    model = Encuesta
    template_name = 'encuestas/encuesta_list.html'
    context_object_name = 'encuestas'
    ordering = ['-fecha_creacion']

class EncuestaCreateView(CreateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name = 'encuestas/encuesta_create.html'
    success_url = reverse_lazy('encuestas:list')

def tomar_encuesta(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    preguntas = encuesta.preguntas.all()

    if request.method == 'POST':
        participante_form = ParticipanteForm(request.POST)
        if participante_form.is_valid():
            participante = participante_form.save()
            for pregunta in preguntas:
                field_name = f"preg_{pregunta.id}"
                # getlist for checkbox/multiple
                valores = request.POST.getlist(field_name)
                if valores:
                    respuesta_texto = '||'.join(valores)
                else:
                    respuesta_texto = request.POST.get(field_name, '')
                Respuesta.objects.create(participante=participante, pregunta=pregunta, respuesta_texto=respuesta_texto)
            return redirect('encuestas:resultados', pk=encuesta.pk)
    else:
        participante_form = ParticipanteForm()
    return render(request, 'encuestas/encuesta_take.html', {'encuesta':encuesta,'preguntas':preguntas,'participante_form':participante_form})

def resumen_encuesta(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    preguntas = encuesta.preguntas.all()
    resumen = []
    for pregunta in preguntas:
        if pregunta.tipo == Pregunta.TIPO_TEXTO:
            respuestas_texto = pregunta.respuestas.values_list('respuesta_texto', flat=True).order_by('-fecha')[:10]
            resumen.append({'pregunta': pregunta, 'tipo': 'texto', 'respuestas': respuestas_texto})
        else:
            contador = {}
            for r in pregunta.respuestas.all():
                if not r.respuesta_texto:
                    continue
                partes = r.respuesta_texto.split('||')
                for p in partes:
                    contador[p] = contador.get(p, 0) + 1
            opciones = pregunta.opciones_list()
            stats = [{'opcion': op, 'count': contador.get(op, 0)} for op in opciones]
            resumen.append({'pregunta': pregunta, 'tipo': 'opcion', 'stats': stats})
    return render(request, 'encuestas/encuesta_results.html', {'encuesta':encuesta,'resumen':resumen})
