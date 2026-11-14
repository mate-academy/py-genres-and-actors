from django.db import models


class Genre(models.Model):
    name = models.CharFieldMax(max_length=255)
