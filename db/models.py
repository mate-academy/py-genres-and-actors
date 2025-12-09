from django.db import models


class Genre(models.Model): # E302: 2 puste linie
    name = models.CharField(max_length=255)

    def __str__(self) -> str: # ANN204: Dodano adnotację typu
        return self.name


class Actor(models.Model): # E302: 2 puste linie
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_actress = models.BooleanField(default=False)

    def __str__(self) -> str: # ANN204: Dodano adnotację typu
        return f"{self.first_name} {self.last_name}"
