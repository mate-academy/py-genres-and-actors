from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%uye0@ybye_v3qsj(*hge-4qk374%6^)j$)0o((tj*n*y5ga1r'


INSTALLED_APPS = [
    "db",
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
