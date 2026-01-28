from django.db import models

MAX_LENGTH = 255


class Genre(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)


class Actor(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
