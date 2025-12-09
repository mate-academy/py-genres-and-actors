from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Pole, które było przyczyną błędu Type Error w testach
    is_actress = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"