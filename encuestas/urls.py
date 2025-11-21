from django.urls import path
from . import views

app_name = 'encuestas'

urlpatterns = [
    path('', views.EncuestaListView.as_view(), name='list'),
    path('encuesta/crear/', views.EncuestaCreateView.as_view(), name='crear'),
    path('encuesta/<int:pk>/tomar/', views.tomar_encuesta, name='tomar'),
    path('encuesta/<int:pk>/resultados/', views.resumen_encuesta, name='resultados'),
]
