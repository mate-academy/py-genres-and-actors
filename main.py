# flake8: noqa: *
import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor

def create_genre(genre_list: list) -> None:
    for genre in genre_list:
        Genre.objects.create(
            name=genre
        )

def create_actor(actor_list: list[tuple]) -> None:
    for first_name, last_name in actor_list:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )


def update_genre(name: str, new_name: str) -> None:
    Genre.objects.filter(
        name=name
    ).update(name=new_name)


def update_actor(info: tuple, new_info: tuple) -> None:
    first_name, last_name = info
    new_first_name, new_last_name = new_info
    Actor.objects.filter(
        first_name=first_name,
        last_name=last_name,
    ).update(
        first_name=new_first_name,
        last_name=new_last_name,
    )


def delete_genre(name: str) -> None:
    Genre.objects.filter(
        name=name
    ).delete()

def delete_actor(info: tuple) -> None:
    first_name, last_name = info
    Actor.objects.filter(
        first_name=first_name,
        last_name=last_name,
    ).delete()


def main() -> QuerySet:
    # Create
    genre_list = ["Western", "Action", "Dramma"]
    actor_list = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    create_genre(genre_list)
    create_actor(actor_list)
    # Update
    change_info = [
        [("George", "Klooney"), ("George", "Clooney")],
        [("Kianu", "Reaves"), ("Keanu", "Reeves")],
    ]
    update_genre("Dramma", "Drama")
    for old_info, new_info in change_info:
        update_actor(old_info, new_info)
    # Delete
    delete_genre("Action")
    for actor in Actor.objects.all():
        if actor.first_name == "Scarlett":
            delete_actor((actor.first_name, actor.last_name))
    # Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")