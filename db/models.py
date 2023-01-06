from django.db import models


class Genres(models.Model):
    name = models.CharField(max_length=255)


class Actors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
