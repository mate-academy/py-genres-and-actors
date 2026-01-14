from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"Genre(id={self.id}, name='{self.name}')"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return (
            f"Actor(id={self.id}, "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}')"
        )
