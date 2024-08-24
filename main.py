import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from typing import Any

from db.models import Genre, Actor


def create_genre(name: str) -> None:
    Genre.objects.create(name=name)


def update_genre(
        new_name: str,
        update_id: int = None,
        name_to_update: str = None,
) -> Genre:
    if update_id:
        return Genre.objects.filter(id=update_id).update(name=new_name)

    if name_to_update:
        return Genre.objects.filter(name=name_to_update).update(name=new_name)

    raise ValueError("Please provide ID or Name of the Genre")


def delete_genre(genre_id: int = None, genre_name: str = None) -> Any:
    if genre_id:
        return Genre.objects.filter(id=genre_id).delete()
    if genre_name:
        return Genre.objects.filter(name=genre_name).delete()


def create_actor(first_name: str, last_name: str) -> None:
    Actor.objects.create(
        first_name=first_name,
        last_name=last_name,
    )


def get_actor_by_id(actor_id: int) -> QuerySet:
    return Actor.objects.filter(id=actor_id)


def get_actor_by_name(
        first_name: str = None,
        last_name: str = None
) -> QuerySet:
    actor = Actor.objects.all()

    if first_name and last_name:
        return actor.filter(first_name=first_name, last_name=last_name)

    if first_name:
        return actor.filter(first_name=first_name)

    if last_name:
        return actor.filter(last_name=last_name)

    raise ValueError("Please provide ID, first or last name of the actor")


def update_actor(
        update_id: int = None,
        first_name: str = None,
        last_name: str = None,
        new_first_name: str = None,
        new_last_name: str = None,
) -> Any:
    if update_id:
        actor = get_actor_by_id(update_id)
    else:
        actor = get_actor_by_name(first_name, last_name)

    if new_first_name and new_last_name:
        return actor.update(first_name=new_first_name, last_name=new_last_name)

    elif new_first_name:
        return actor.update(first_name=new_first_name)

    elif new_last_name:
        return actor.update(last_name=new_last_name)


def delete_actor(
        actor_id: int = None,
        first_name: str = None,
        last_name: str = None
) -> tuple[Any, Any]:
    if actor_id:
        return Actor.objects.filter(id=actor_id).delete()

    return get_actor_by_name(first_name, last_name).delete()


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for genre_name in genres:
        create_genre(genre_name)

    for first_name, last_name in actors:
        create_actor(first_name, last_name)

    update_genre("Drama", name_to_update="Dramma")

    update_actor(
        first_name="George",
        last_name="Klooney",
        new_last_name="Clooney"
    )

    update_actor(
        first_name="Kianu",
        last_name="Reaves",
        new_first_name="Keanu",
        new_last_name="Reeves"
    )

    delete_genre(genre_name="Action")

    delete_actor(first_name="Scarlett")

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
