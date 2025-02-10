import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor
from db.models import Genre


def main() -> QuerySet:
    create_actor([("George", "Klooney"), ("Kianu", "Reaves"),
                  ("Scarlett", "Keegan"), ("Will", "Smith"),
                  ("Jaden", "Smith"), ("Scarlett", "Johansson"),
                  ("Scarlett", "Johansson")])

    create_genre(["Western", "Action", "Dramma"])

    Genre.objects.filter(
        name="Dramma"
    ).update(
        name="Drama",
    )

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney",
    ).update(
        last_name="Clooney"
    )

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")


def create_actor(profiles: list) -> None:
    for profile in profiles:
        Actor.objects.create(
            first_name=profile[0],
            last_name=profile[1],
        )


def create_genre(genres: list) -> None:
    for gen in genres:
        Genre.objects.create(
            name=gen,
        )
