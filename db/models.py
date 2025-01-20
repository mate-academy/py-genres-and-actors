from django.db import models


class Genre(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=255)
=======
    genre_name = models.CharField(max_length=255)
>>>>>>> b2582479ebab56ab307457b545a068a061971d82


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
<<<<<<< HEAD
    last_name = models.CharField(max_length=255)
=======
    last_name = models.CharField(max_length=255)
>>>>>>> b2582479ebab56ab307457b545a068a061971d82
