import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor
from db.models import Genre


def main() -> QuerySet:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",)
    ]

    for genre in genres:
        Genre.objects.create(
            name=genre[0]
        )

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for actor in actors:
        Actor.objects.create(
            first_name=actor[0],
            last_name=actor[1]
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

    actors_with_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    for actor in actors_with_smith:
        print(actor)

    return actors_with_smith
