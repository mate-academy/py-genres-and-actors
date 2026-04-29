import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    genres = [
        Genre(name=item) for item in genres
    ]
    actors = [
        Actor(first_name=name, last_name=surname)
        for name, surname in actors
    ]

    # 1. CREATE
    Genre.objects.bulk_create(genres)
    Actor.objects.bulk_create(actors)

    # 2. UPDATE
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # 3. DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. READ
    smiths = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smiths
