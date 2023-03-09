from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Band(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)


class Album(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True, blank=True)


class Concert(models.Model):
    name = models.CharField(max_length=63)
    audience = models.IntegerField(default=100)
