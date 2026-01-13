from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Actor(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)

    def __str__(self) -> None:
        return f"{self.first_name} {self.last_name}"
