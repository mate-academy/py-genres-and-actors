from django.db import models
from dataclasses import dataclass


@dataclass
class Genre(models.Model):
    name = models.CharField(max_length=255)


@dataclass
class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
