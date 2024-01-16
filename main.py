from typing import List
from django.db.models import QuerySet
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

django.setup()

from db.models import Genre, Actor  # noqa E402


def create_genres(genre_names: List[str]) -> List[Genre]:
    return [Genre.objects.create(
        name=genre_name
    ) for genre_name in genre_names]


def create_actors(actors_data: List[dict]) -> List[Actor]:
    return [Actor.objects.create(**actor_data) for actor_data in actors_data]


def main() -> QuerySet[Actor]:
    # Create genres
    genre_names = ["Western", "Action", "Dramma"]
    create_genres(genre_names)

    # Create actors
    actors_data = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]
    create_actors(actors_data)

    # Update genres
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Update actors
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # Delete
    Genre.objects.get(name="Action").delete()

    actresses_scarlett = Actor.objects.filter(first_name="Scarlett")
    actresses_scarlett.delete()

    # Return
    actors_with_last_name_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return actors_with_last_name_smith
