from django.db import models


class Genre(models.Model):
    name = models.Field(max_length=255)


class Actor(models.Model):
    first_name = models.Field(max_length=255)
    last_name = models.Field(max_length=255)
