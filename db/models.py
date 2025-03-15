from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return (f"Genre: {self.name}, "
                f"ID: {self.id}")


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return (f"First name: {self.first_name}, "
                f"Last Name: {self.last_name}, "
                f"ID: {self.id}")
