import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "super-secret-key-just-for-testing"

DEBUG = False

ALLOWED_HOSTS = []
INSTALLED_APPS = [
    # Poprawka Q000: użycie podwójnych cudzysłowów
    "django.contrib.contenttypes",
    "django.contrib.auth",

    # Poprawka Q000: użycie podwójnych cudzysłowów
    "db.apps.DbConfig",
]

DATABASES = {
    "default": {
        # Poprawka Q000: użycie podwójnych cudzysłowów
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
# Poprawka Q000: użycie podwójnych cudzysłowów
ROOT_URLCONF = "main"

USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SILENCED_SYSTEM_CHECKS = ["urls.W002"]
# W292: Została dodana nowa linia na końcu pliku002"]