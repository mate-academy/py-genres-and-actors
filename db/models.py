from django.db import models


class Genre:
    name = models.CharField(max_length=255)

    def __str__(self) -> chr:
        return self.name

class Actor:
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
