import init_django_orm  # noqa: F401

from django.db import models

from db.models import Actor, Genre


def create() -> None:
    new_genres = ["Western", "Action", "Dramma"]
    for genre in new_genres:
        Genre.objects.create(name=genre)

    new_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first, last in new_actors:
        Actor.objects.create(first_name=first, last_name=last)


def update() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")

    list_of_actors_updates = [
        [("George", "Klooney"), ("George", "Clooney")],
        [("Kianu", "Reaves"), ("Keanu", "Reeves")]
    ]
    for old_actor, new_actor in list_of_actors_updates:
        old_first, old_last = old_actor
        new_first, new_last = new_actor
        Actor.objects.filter(
            first_name=old_first, last_name=old_last
        ).update(first_name=new_first, last_name=new_last)


def delete() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def main() -> models.QuerySet:

    create()

    update()

    delete()

    set_of_actors = Actor.objects.filter(
        last_name="Smith").order_by("first_name")
    return set_of_actors
