import init_django_orm  # noqa: F401

from db.models import Genre, Actor
from django.db.models import QuerySet

list_of_genres = [
    "Western", "Action", "Dramma"
]

list_of_actors = [
    {
        "first_name": "George",
        "last_name": "Klooney"
    },
    {
        "first_name": "Kianu",
        "last_name": "Reaves"
    },
    {
        "first_name": "Scarlett",
        "last_name": "Keegan"
    },
    {
        "first_name": "Will",
        "last_name": "Smith"
    },
    {
        "first_name": "Jaden",
        "last_name": "Smith"
    },
    {
        "first_name": "Scarlett",
        "last_name": "Johansson"
    },

]


def main() -> QuerySet:

    for genre in list_of_genres:
        Genre.objects.create(
            name=f"{genre}"
        )

    for actor in list_of_actors:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )
    # genre Dramma, set `name` to "Drama"
    Genre.objects.filter(
        name="Dramma"
    ).update(
        name="Drama"
    )
    # actor George Klooney, set `last_name` to "Clooney"
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    # actor Kianu Reaves, set `first_name`
    # to "Keanu" and `last_name` to "Reeves"
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )
    # Delete genre Action
    Genre.objects.filter(
        name="Action"
    ).delete()
    # Delete all actresses with the `first_name` "Scarlett"
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()
    # Return QuerySet of actors with `last_name`
    # "Smith" and ordered by `first_name`
    query = Actor.objects.filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    )
    return query
