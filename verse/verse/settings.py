"""
Verse Django settings file

It uses `python-decouple` and `dj-database-url` libraries to get instance
specific config from '.env' file and environment variables
"""
from pathlib import Path

from decouple import config
from dj_database_url import parse as db_url


BASE_DIR = Path(__file__).parent.parent.parent


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='localhost, 127.0.0.1',
    cast=lambda l: [s.strip() for s in l.split(',')],
)


ROOT_URLCONF = 'verse.urls'

WSGI_APPLICATION = 'verse.wsgi.application'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'verse',
    'checkers',
    'projects',

    'django_redis',
    'rest_framework',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + str(BASE_DIR.joinpath('db.sqlite3')),
        cast=db_url,
    )
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config(
            'REDIS_CACHE_URL', default='redis://127.0.0.1:6379/0',
        ),
        'TIMEOUT': 60 * 60 * 24,  # 1 day
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}


MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))


LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Misc
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


#############################
# Third-party apps settings #
#############################

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': (
        'rest_framework.versioning.AcceptHeaderVersioning'
    ),
}

# Celery
CELERY_BROKER_URL = config(
    'CELERY_BROKER_URL',
    default='redis://127.0.0.1:6379/1',
)
CELERY_TASK_IGNORE_RESULT = True
