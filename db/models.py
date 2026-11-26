from django.db import models


class Genre(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class Actor(models.Model):
    objects = models.Manager()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
