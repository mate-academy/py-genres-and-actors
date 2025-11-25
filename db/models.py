from django.db import models


class Genre(models.Model):
    """
    Represents a genre in the system.

    This class is used to store genre details, such as its name.
    It extends the Django `models.Model` class and is typically
    used in applications where genre information needs to be
    categorized or displayed.

    :ivar name: The name of the genre.
    :type name: str
    """
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    """
    Represents an Actor entity.

    This class is used to define the Actor model, containing
    basic information about an actor such as their first and last names.
    The purpose of this class is to serve as a Django model that interacts
    with the database and providesa representation of an actor in the system.

    :ivar first_name: The first name of the actor.
    :type first_name: str
    :ivar last_name: The last name of the actor.
    :type last_name: str
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
