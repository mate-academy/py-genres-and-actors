import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

GENRES = ["Western", "Action", "Dramma"]
ACTORS = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def main() -> QuerySet:
    create()
    update()
    delete()
    return read()


def create() -> None:
    for genre in GENRES:
        Genre.objects.create(name=genre)
    for name, surname in ACTORS:
        Actor.objects.create(first_name=name, last_name=surname)


def update() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")


def delete() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def read() -> QuerySet:
    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return smith_actors
