from django.db import models


class Genre(models.Model):
    name = models.CharFieldMax(max_length=255)


class Actor(models.Model):
    first_name = models.CharFieldMax(max_length=255)
    last_name = models.CharFieldMax(max_length=255)
