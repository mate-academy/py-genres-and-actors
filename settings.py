import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'super-secret-key-just-for-testing'

DEBUG = False

ALLOWED_HOSTS = []

# KLUCZOWE USTAWIENIE: Rejestracja aplikacji
INSTALLED_APPS = [
    # Wymagane podstawowe komponenty Django do poprawnego działania ORM
    'django.contrib.contenttypes',
    'django.contrib.auth',

    # Twoja aplikacja (poprawna ścieżka do klasy konfiguracyjnej DbConfig)
    "db.apps.DbConfig",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Konfiguracja dla pytest-django
ROOT_URLCONF = 'main'

USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SILENCED_SYSTEM_CHECKS = ["urls.W002"]