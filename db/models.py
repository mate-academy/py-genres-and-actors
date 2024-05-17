from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Genre: {self.name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return (f"Actor (first name: {self.first_name}, "
                f"last name: {self.last_name}")
