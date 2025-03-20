import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor
from typing import Tuple, List


def main() -> QuerySet:
    genres: List[str] = ["Western", "Action", "Dramma"]
    actors: List[Tuple[str, str]] = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
