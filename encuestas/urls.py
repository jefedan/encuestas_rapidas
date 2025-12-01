# appEncuestas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('admin/panel/', views.admin_panel, name='admin_panel'),
    path('usuario/panel/', views.usuario_panel, name='usuario_panel'),

    # CRUD Encuesta
    path('admin/encuestas/', views.encuesta_list, name='encuesta_list'),
    path('admin/encuestas/nueva/', views.encuesta_create, name='encuesta_create'),
    path('admin/encuestas/<int:id_encuesta>/editar/', views.encuesta_update, name='encuesta_update'),
    path('admin/encuestas/<int:id_encuesta>/eliminar/', views.encuesta_delete, name='encuesta_delete'),

    # CRUD Pregunta
    path('admin/preguntas/', views.pregunta_list, name='pregunta_list'),
    path('admin/preguntas/nueva/', views.pregunta_create, name='pregunta_create'),
    path('admin/preguntas/<int:id_pregunta>/editar/', views.pregunta_update, name='pregunta_update'),
    path('admin/preguntas/<int:id_pregunta>/eliminar/', views.pregunta_delete, name='pregunta_delete'),

    # CRUD Participante
    path('admin/participantes/', views.participante_list, name='participante_list'),
    path('admin/participantes/nuevo/', views.participante_create, name='participante_create'),
    path('admin/participantes/<int:id_participante>/editar/', views.participante_update, name='participante_update'),
    path('admin/participantes/<int:id_participante>/eliminar/', views.participante_delete, name='participante_delete'),

    # Responder encuesta (usuario)
    path('usuario/encuestas/', views.encuestas_asignadas, name='encuestas_asignadas'),
    path('usuario/encuestas/<int:id_encuesta>/', views.responder_encuesta, name='responder_encuesta'),

    # Estadística
    path('admin/encuestas/<int:id_encuesta>/resumen/', views.resumen_encuesta, name='resumen_encuesta'),
]

