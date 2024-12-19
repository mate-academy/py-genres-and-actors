from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.genre


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
