from __future__ import annotations
import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # create Genre
    for name in ("Western", "Action", "Dramma"):
        genre = Genre(name=name)
        genre.save()

    # create Actor
    actors = (
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    )

    for first_name, last_name in actors:
        actor = Actor(first_name=first_name, last_name=last_name)
        actor.save()

    # update Genre
    dramma = Genre.objects.filter(name="Dramma")
    dramma.update(name="Drama")

    # update Actor
    klooney = Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    )
    klooney.update(last_name="Clooney")

    kianu = Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    )

    kianu.update(first_name="Keanu", last_name="Reeves")

    # delete Genre
    Genre.objects.filter(name="Action").delete()

    # delete Actor
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
