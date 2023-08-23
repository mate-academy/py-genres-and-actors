import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    for genre_str in ("Western", "Action", "Dramma"):
        Genre.objects.create(name=genre_str)

    for actor_str in (
            "George Klooney",
            "Kianu Reaves",
            "Scarlett Keegan",
            "Will Smith",
            "Jaden Smith",
            "Scarlett Johansson"
    ):
        first_name, last_name = actor_str.split()[0], actor_str.split()[1]
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
