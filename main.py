import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Clear existing data to avoid duplicates
    Genre.objects.all().delete()
    Actor.objects.all().delete()

    # --- Genres ---
    genre_names = [("Western",), ("Action",), ("Dramma",)]
    for (name,) in genre_names:
        Genre.objects.create(name=name)

    # --- Actors ---
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # --- Updates ---
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # --- Deletions ---
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # --- Return Smiths ordered by first name ---
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
