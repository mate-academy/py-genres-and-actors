from django.db.models import Model, CharField


class Genre(Model):
    name = CharField(max_length=255)

    def __str__(self) -> str:
        return f"Genre with name: {self.name}"


class Actor(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)

    def __str__(self) -> str:
        return f"Actor: {self.first_name} {self.last_name}"
