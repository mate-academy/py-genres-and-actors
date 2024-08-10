import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    create_genres()
    create_actors()
    update()
    delete()
    return specific_actors()


def create_genres() -> None:
    for name in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=name)


def create_actors() -> None:
    actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]
    for actor in actors:
        first_name, last_name = actor.split()
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")


def delete() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def specific_actors() -> QuerySet:
    actors_smith = Actor.objects.filter(last_name="Smith")
    return actors_smith.order_by("first_name")
