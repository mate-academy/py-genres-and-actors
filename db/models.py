from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self) -> str:
        return f"<Genre: {self.name}>"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def _str_(self) -> str:
        name = f"{self.first_name}"
        last = f"{self.last_name}"
        return f"<Actor: {name} {last}>"
