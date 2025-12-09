from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)  # E261: Dodano dwie spacje

    def __str__(self) -> str:
        return self.name  # E261: Dodano dwie spacje


class Actor(models.Model):
    first_name = models.CharField(max_length=255)  # E261: Dodano dwie spacje
    last_name = models.CharField(max_length=255)
    is_actress = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"  # E261: Dodano dwie spacje
