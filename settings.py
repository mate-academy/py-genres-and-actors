import os
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent

SECRET_KEY: str = os.environ.get("DJANGO_SECRET_KEY", "dev-secret")

DEBUG: bool = True

ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "db",  # ваш додаток
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES: dict[str, dict[str, str]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("DB_NAME", ":memory:"),
    }
}

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"

STATIC_URL: str = "/static/"
