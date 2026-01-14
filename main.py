import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def create_genres(genres: list[str]) -> None:
    for genre_name in genres:
        Genre.objects.create(name=genre_name)


def create_actors(actors: list[tuple[str, str]]) -> None:
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_records() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )


def delete_records() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    create_genres(genres)
    create_actors(actors)
    update_records()
    delete_records()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
