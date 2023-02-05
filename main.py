import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor

some_actors = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]

some_genres = [
    "Western", "Action", "Dramma"
]


def main() -> QuerySet:
    for genre in some_genres:
        Genre.objects.create(
            name=genre
        )

    for first_n, last_n in some_actors:
        Actor.objects.create(
            first_name=first_n,
            last_name=last_n
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
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
