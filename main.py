import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    create_genre()
    create_actor()
    update_genre()
    update_actors()
    delete_genre()
    delete_actors()
    return return_actors()


def create_genre() -> None:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)


def create_actor() -> None:
    actors = [
        ["George", "Klooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"]
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_genre() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")


def update_actors() -> None:
    Actor.objects.filter(
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    )

    Actor.objects.filter(
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )


def delete_genre() -> None:
    Genre.objects.filter(name="Action").delete()


def delete_actors() -> None:
    Actor.objects.filter(first_name="Scarlett").delete()


def return_actors() -> None:
    actors = Actor.objects.filter(last_name="Smith")
    return actors.order_by("first_name")
