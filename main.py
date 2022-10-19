import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    create_genre("Western", "Action", "Dramma")
    create_actor(
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    )

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def create_genre(*genres: str) -> None:
    for genre in genres:
        Genre.objects.create(name=genre)


def create_actor(*actors: tuple[str, str]) -> None:
    for actor in actors:
        actors_first_name, actors_last_name = actor
        Actor.objects.create(
            first_name=actors_first_name,
            last_name=actors_last_name
        )
