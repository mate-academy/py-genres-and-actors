import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]

    actors_name = ["George", "Kianu", "Scarlett",
                   "Will", "Jaden", "Scarlett"]
    actors_surname = ["Klooney", "Reaves", "Keegan",
                      "Smith", "Smith", "Johansson"]

    for genre in genres:
        Genre.objects.create(
            name=genre
        )

    for actors_name, actors_surname in zip(actors_name, actors_surname):
        Actor.objects.create(
            first_name=actors_name,
            last_name=actors_surname
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
