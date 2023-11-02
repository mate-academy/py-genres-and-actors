import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor
from data import GENRES, ACTORS


def main() -> QuerySet:
    for genre in GENRES:
        Genre.objects.create(
            name=genre
        )

    for actor in ACTORS:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
