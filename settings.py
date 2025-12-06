import os
from pathlib import Path
from typing import Any


BASE_DIR: Path = Path(__file__).resolve().parent

SECRET_KEY: str = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret')

DEBUG: bool = True

ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS: list[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'db',  # ваш додаток
]

MIDDLEWARE: list[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF: str = 'project.urls'

TEMPLATES: list[dict[str, Any]] = [
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

WSGI_APPLICATION: str = 'project.wsgi.application'

DATABASES: dict[str, dict[str, Any]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

STATIC_URL: str = '/static/'
