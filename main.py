import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def create_genres() -> None:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]

    for genre in genres:
        Genre.objects.create(name=genre[0])


def create_actors() -> None:
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for actor in actors:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])


def update_genre_name() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")


def update_actor_name() -> None:
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )


def delete_genre_and_actors() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def get_filtered_actors() -> QuerySet:
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def main() -> QuerySet:
    create_genres()
    create_actors()

    update_genre_name()
    update_actor_name()

    delete_genre_and_actors()

    return get_filtered_actors()
