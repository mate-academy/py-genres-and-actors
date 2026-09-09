from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=235)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=235)
    last_name = models.CharField(max_length=235)

    def str(self) -> str:
        return f"{self.first_name} {self.last_name}"
