from django.db import models


class Genre(models.Model):
    """Class Genre represents movie's category"""

    name = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return str(self.name)


class Actor(models.Model):
    """Class Actor is  cinema actor/actress"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
