from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"<Genre: {self.name}>"


class Actor(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"<Actor: {self.first_name} {self.last_name}>"
