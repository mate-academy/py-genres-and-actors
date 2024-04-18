import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    tables_create()
    tables_update()
    tables_delete()

    actors_smiths_query = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return actors_smiths_query


def tables_delete() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def tables_update() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")


def tables_create() -> None:
    genres_to_create = ["Western", "Action", "Dramma"]
    actors_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for genre in genres_to_create:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name)
