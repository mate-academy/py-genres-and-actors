from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import Actor, Genre


def create_genres(genres: list) -> None:
    Genre.objects.bulk_create(
        [Genre(name=genre) for genre in genres],
        ignore_conflicts=True
    )


def create_actors(actors: list[tuple[str, str]]) -> None:
    Actor.objects.bulk_create(
        [
            Actor(
                first_name=first_name,
                last_name=last_name
            ) for first_name, last_name in actors
        ],
        ignore_conflicts=True
    )


def update_genres_name(old_name: str, new_name: str) -> None:
    Genre.objects.filter(name=old_name).update(name=new_name)


def update_actors_name(
        old_first_name: str,
        new_first_name: str,
        old_last_name: str,
        new_last_name: str
) -> None:
    Actor.objects.filter(
        first_name=old_first_name,
        last_name=old_last_name
    ).update(
        first_name=new_first_name,
        last_name=new_last_name
    )


def delete_genre(name: str) -> None:
    Genre.objects.filter(name=name).delete()


def delete_actors(first_name: str) -> None:
    Actor.objects.filter(first_name=first_name).delete()


def get_actors_with_last_name(last_name: str) -> QuerySet:
    return Actor.objects.filter(last_name=last_name).order_by("first_name")


def main() -> QuerySet:
    pass
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

    update_genres_name("Dramma", "Drama")
    update_actors_name("George", "George", "Klooney", "Clooney")
    update_actors_name("Kianu", "Keanu", "Reaves", "Reeves")

    delete_genre("Action")
    delete_actors("Scarlett")

    return get_actors_with_last_name("Smith")
