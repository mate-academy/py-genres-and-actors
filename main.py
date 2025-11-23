import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_names = ("Western", "Action", "Dramma")
    for genre_name in genre_names:
        Genre.objects.get_or_create(name=genre_name)

    actor_first_and_last_names = (("George", "Klooney"),
                                  ("Kianu", "Reaves"),
                                  ("Scarlett", "Keegan"),
                                  ("Will", "Smith"),
                                  ("Jaden", "Smith"),
                                  ("Scarlett", "Johansson"))
    for first_name, last_name in actor_first_and_last_names:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return smith_actors
