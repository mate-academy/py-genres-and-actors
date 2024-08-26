from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def create_data() -> None:
    new_genres = ["Western", "Action", "Dramma"]
    for genre in new_genres:
        Genre.objects.create(name=genre)

    new_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in new_actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_data() -> None:
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"

    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )


def delete_data() -> None:
    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()


def get_result() -> QuerySet:
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")


def main() -> QuerySet:
    create_data()
    update_data()
    delete_data()

    return get_result()
