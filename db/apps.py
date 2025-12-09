# db/apps.py
from django.apps import AppConfig

class DbConfig(AppConfig):
    name = 'db'
    default_auto_field = 'django.db.models.BigAutoField'