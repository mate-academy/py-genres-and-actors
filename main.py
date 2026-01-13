import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def create() -> None:
    genres = ["Western", "Action", "Dramma"]

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )


def delete() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def sort_by() -> QuerySet:
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def main() -> QuerySet:
    create()
    update()
    delete()
    return sort_by()
