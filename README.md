# Encuestas Rápidas (Django) - Versión Completa (Admin mejorado)
Proyecto demo listo para abrir en GitHub Codespaces.

Contenido principal:
- App `encuestas` con modelos: Encuesta, Pregunta, Respuesta, Participante
- Vistas para crear encuestas (frontend simple), tomar encuestas y ver resultados
- Admin mejorado con inlines, búsqueda y filtros
- Comando para crear datos de ejemplo
- .devcontainer para Codespaces

Instrucciones rápidas (local o Codespaces):
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py create_sample_data
  python manage.py runserver 0.0.0.0:8000

Nota: db.sqlite3 no se incluye por seguridad; se genera con migrate.
