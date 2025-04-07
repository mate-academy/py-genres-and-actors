import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:

    genres = ["Action", "Comedy", "Drama"]
    for genre_name in genres:
        Genre.objects.get_or_create(name=genre_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Genre.objects.filter(name="Action").delete()

    actors = [
        {"first_name": "Keanu", "last_name": "Reeves"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
        {"first_name": "Brad", "last_name": "Pitt"},
    ]
    for actor_data in actors:
        Actor.objects.get_or_create(**actor_data)


    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
