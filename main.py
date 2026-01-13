import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    for genre in ["Western", "Action", "Dramma"]:
        Genre.objects.create(
            name=genre
        )

    for actor in ["George Klooney", "Kianu Reaves",
                  "Scarlett Keegan", "Will Smith",
                  "Jaden Smith", "Scarlett Johansson"]:
        first_n = actor.split()[0]
        last_n = actor.split()[-1]
        Actor.objects.create(
            first_name=first_n,
            last_name=last_n,
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="George",
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
        first_name="Scarlett",
    ).delete()

    list_of_actors = Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")

    return list_of_actors
