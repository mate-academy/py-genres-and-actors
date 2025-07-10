import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def create() -> None:
    genre = ["Western", "Action", "Dramma"]
    for name in genre:
        Genre.objects.create(name=name)
    actor = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]
    for full_name in actor:
        first_name, last_name = full_name.split()
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update() -> None:
    (Genre.objects.
     filter(name="Dramma").
     update(name="Drama"))
    (Actor.objects.
     filter(first_name="George", last_name="Klooney").
     update(last_name="Clooney"))
    (Actor.objects.
     filter(first_name="Kianu", last_name="Reaves").
     update(first_name="Keanu", last_name="Reeves"))


def delete() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def main() -> QuerySet:
    create()
    update()
    delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
