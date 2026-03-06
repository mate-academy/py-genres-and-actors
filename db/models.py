from django.db.models import Model, CharField


class Genre(Model):
    name = CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
