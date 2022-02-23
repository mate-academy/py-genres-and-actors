from django.db import models


class Genre(models.Model):
    _name_max_length = 255
    name = models.CharField(
        max_length=_name_max_length
    )


class Actor(models.Model):
    _first_name_max_length = 255
    _last_name_max_length = 255
    first_name = models.CharField(
        max_length=_first_name_max_length
    )
    last_name = models.CharField(
        max_length=_last_name_max_length
    )
