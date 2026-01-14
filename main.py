import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ("Western", "Action", "Dramma")
    actors = (
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    )

    # 1. Create
    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # 2. Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        first_name="George",
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # 3. Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
