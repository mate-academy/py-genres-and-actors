from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=25)


class Actor(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
