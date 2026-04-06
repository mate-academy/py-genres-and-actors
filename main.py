from typing import Any

import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet[Any]:
    for name in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for actor in actors:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    actor = Actor.objects.get(first_name="George", last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()

    actor = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
