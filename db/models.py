from django.db import models


class Genre(models.Model):
    """Movie genre model."""

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Return the genre name."""
        return self.name


class Actor(models.Model):
    """Movie actor model."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Return the actor's full name."""
        return f"{self.first_name} {self.last_name}"
