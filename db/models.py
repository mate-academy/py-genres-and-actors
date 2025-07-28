from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
