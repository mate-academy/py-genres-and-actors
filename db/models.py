from django.db import models
from typing import Any


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> Any:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
