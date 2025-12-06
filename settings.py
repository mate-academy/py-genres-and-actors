import os
from pathlib import Path
from typing import Any


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
    "django.contrib.
