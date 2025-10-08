from django.db import models
from django.core.management import call_command

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


call_command("makemigrations", "db", interactive=False)
call_command("migrate", interactive=False)