from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)  # Збільшено до 255 символів


class Actor(models.Model):
    first_name = models.CharField(max_length=255)  # Збільшено до 255 символів
    last_name = models.CharField(max_length=255)  # Збільшено до 255 символів
