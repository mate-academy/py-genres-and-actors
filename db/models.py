from django.db import models


class Genre(models.Model):
    """Create table genre"""
    name = models.CharField(max_length=255)


class Actor(models.Model):
    """Create table actor"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
