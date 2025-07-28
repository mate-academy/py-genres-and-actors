from django.db import models


class Genre(models.Model):
    name = models.CharField(max_len=255)


class Actor(models.Model):
    first_name = models.CharField(max_len=255)
    last_name = models.CharField(max_len=255)