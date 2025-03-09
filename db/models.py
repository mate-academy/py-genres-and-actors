from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "genre"
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("first_name", "last_name")
        db_table = "actor"
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
