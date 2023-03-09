import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor
from db.data import GENRES, ACTORS


def main() -> QuerySet:

    for genre in GENRES:
        Genre.objects.create(name=genre)

    for actor in ACTORS:
        first_name, last_name = actor
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
