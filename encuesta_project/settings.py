from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- CONFIG BÁSICA ---
SECRET_KEY = 'clave-super-secreta-para-pruebas'  # puedes cambiarla
DEBUG = True
ALLOWED_HOSTS = []   # en desarrollo puede estar vacío

# --- APLICACIONES INSTALADAS ---
INSTALLED_APPS = [
    # 'django.contrib.admin',  # puedes activarlo si quieres usar admin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appEncuestas',
]

# --- MIDDLEWARE (OBLIGATORIO) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URL PRINCIPAL DEL PROYECTO ---
ROOT_URLCONF = 'Encuestas.urls'

# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],          # usamos templates dentro de las apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- WSGI (para despliegue, igual Django lo pide) ---
WSGI_APPLICATION = 'Encuestas.wsgi.application'

# --- BASE DE DATOS: MySQL ---

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'encuestas',
        'USER': 'postgres',      # o el usuario que uses
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# --- CONFIG IDIOMA / HORA ---
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_TZ = True

# --- STATIC ---
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
