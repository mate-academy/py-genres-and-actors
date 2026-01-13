import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Genre, Actor


def create_genres() -> None:
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)


def create_actors() -> None:
    actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]
    for actor in actors:
        first_name, last_name = actor.split()
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_genre_name(old_name: str, new_name: str) -> None:
    Genre.objects.filter(name=old_name).update(name=new_name)


def update_actor_name(
        first_name: str,
        old_last_name: str,
        new_first_name: str,
        new_last_name: str
) -> None:
    Actor.objects.filter(
        first_name=first_name,
        last_name=old_last_name
    ).update(
        first_name=new_first_name,
        last_name=new_last_name
    )


def delete_genre(name: str) -> None:
    Genre.objects.filter(name=name).delete()


def delete_actors_by_first_name(first_name: str) -> None:
    Actor.objects.filter(first_name=first_name).delete()


def main() -> QuerySet:
    create_genres()
    create_actors()

    update_genre_name("Dramma", "Drama")
    update_actor_name("George", "Klooney", "George", "Clooney")
    update_actor_name("Kianu", "Reaves", "Keanu", "Reeves")

    delete_genre("Action")
    delete_actors_by_first_name("Scarlett")

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
