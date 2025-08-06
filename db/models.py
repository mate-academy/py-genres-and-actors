from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.birth_year})"
