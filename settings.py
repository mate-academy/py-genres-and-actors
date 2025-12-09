import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "super-secret-key-just-for-testing"

DEBUG = False

ALLOWED_HOSTS = []
INSTALLED_APPS = [
    # Wymagane komponenty Django
    "django.contrib.contenttypes",
    "django.contrib.auth",

    # Twoja aplikacja
    "db.apps.DbConfig",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
# Użyto podwójnych cudzysłowów dla ROOT_URLCONF
ROOT_URLCONF = "main"

USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SILENCED_SYSTEM_CHECKS = ["urls.W002"]
