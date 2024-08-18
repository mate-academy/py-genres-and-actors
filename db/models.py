from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length = 250)
    print(name)


class Actor(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
