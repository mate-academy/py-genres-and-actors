from django.db import models


class Genre(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255)


class Actor(models.Model):
    objects = models.Manager
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
