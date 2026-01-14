from django.db import models
from django.db.models import CharField


class Genre(models.Model):
    name = CharField(max_length=255)


class Actor(models.Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
