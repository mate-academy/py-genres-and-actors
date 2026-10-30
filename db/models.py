from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=120)


class Actor(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
