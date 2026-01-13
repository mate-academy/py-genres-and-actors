from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class Actor(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        null=False,
        blank=False,
        default="not defined"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
