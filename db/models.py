from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = "db"

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        app_label = "db"
        unique_together = ("first_name", "last_name")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    class Meta:
        app_label = "db"

    def __str__(self) -> str:
        return f"{self.title} ({self.release_year})"
