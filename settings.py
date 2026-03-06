from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Make sure 'db' is in INSTALLED_APPS so Django sees your models
INSTALLED_APPS = [
    "db",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SECRET_KEY = "fake-key-for-tests"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
