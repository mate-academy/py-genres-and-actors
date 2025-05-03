import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # 1
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.get_or_create(name=genre)
    actors = ["George Klooney", "Kianu Reaves", "Scarlett Keegan",
              "Will Smith", "Jaden Smith", "Scarlett Johansson"]
    for actor in actors:
        (name, surname) = actor.split(" ", 1)
        Actor.objects.get_or_create(first_name=name, last_name=surname)

    # 2
    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(first_name="George", last_name="Klooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))

    # 3
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
