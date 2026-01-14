import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    new_genres = ["Western", "Action", "Dramma"]
    new_actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]

    # Create
    for genre in new_genres:
        Genre.objects.create(name=genre)

    for actor in new_actors:
        actors_name = actor.split()
        Actor.objects.create(first_name=actors_name[0],
                             last_name=actors_name[1])

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(first_name="Keanu").update(last_name="Reeves")

    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Read
    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return actors
