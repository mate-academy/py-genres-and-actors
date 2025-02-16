import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        Genre(name="Western"),
        Genre(name="Drama")
    ]
    Genre.objects.bulk_create(genres)

    actors = [
        Actor(first_name="George", last_name="Clooney"),
        Actor(first_name="Keanu", last_name="Reeves"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith")
    ]
    Actor.objects.bulk_create(actors)

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
