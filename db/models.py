from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
