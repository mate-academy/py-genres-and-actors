import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    create_genres(["Western", "Action", "Dramma"])
    create_actors([
        ["George", "Klooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"],
    ])
    update_genre("Dramma", "Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves",
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def create_genres(genres: list) -> None:
    for genre in genres:
        Genre.objects.create(name=genre)


def create_actors(actors: list) -> None:
    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )


def update_genre(genre: str, updated_genre: str) -> None:
    Genre.objects.filter(name=genre).update(name=updated_genre)
