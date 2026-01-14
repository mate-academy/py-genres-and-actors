from django.db.models import Model, CharField


class Genre(Model):
    name = CharField(max_length=255)


class Actor(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
