from django.db import models


class Genre(models.Model):
    name: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    name: str = models.CharField(max_length=100)
    surname: str = models.CharField(max_length=100)
    age: int = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
