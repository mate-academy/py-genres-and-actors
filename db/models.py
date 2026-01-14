from django.db import models


class Genre(models.Model):
    """Genre model representing movie genres."""
    name = models.CharField(max_length=255)

    def __str__(self) -> None:
        """String representation of Genre."""
        return self.name


class Actor(models.Model):
    """Actor model representing actors and actresses."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> None:
        """String representation of Actor."""
        return f"{self.first_name} {self.last_name}"
