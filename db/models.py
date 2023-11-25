from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Genre: {Genre.name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"Actor: {Actor.first_name} {Actor.last_name}"
