import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor
from db.models import Genre


def main() -> QuerySet:

    # create genre
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(
            name=genre,
        )

    # create actor
    actors = ["George Klooney", "Kianu Reaves", "Scarlett Keegan",
              "Will Smith", "Jaden Smith", "Scarlett Johansson"]
    for actor in actors:
        Actor.objects.create(
            first_name=" ".join(actor.split(" ")[:1]),
            last_name=" ".join(actor.split(" ")[1:])
        )

    # update genre
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # update actor
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney"),

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves"),

    # delete genre
    Genre.objects.filter(name="Action").delete()

    # delete actor
    Actor.objects.filter(first_name="Scarlett").delete()

    # order_by first_name
    actors_order_by = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return actors_order_by
