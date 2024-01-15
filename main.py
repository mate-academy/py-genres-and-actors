from typing import List
from django.db.models import QuerySet
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

django.setup()

from db.models import Genre, Actor  # noqa E402


def create_genres(genre_names: List[str]) -> List[Genre]:
    created_genres = []
    for genre_name in genre_names:
        genre = Genre.objects.create(name=genre_name)
        created_genres.append(genre)
    return created_genres


def create_actors(actors_data: List[dict]) -> List[Actor]:
    created_actors = []
    for actor_data in actors_data:
        actor = Actor.objects.create(**actor_data)
        created_actors.append(actor)
    return created_actors


def main() -> QuerySet[Actor]:
    # Create genres
    genre_names = ["Western", "Action", "Dramma"]  # noqa
    created_genres = create_genres(genre_names)

    # Create actors
    actors_data = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]
    created_actors = create_actors(actors_data)

    # Update
    for genre in created_genres:  # noqa
        if genre.name == "Dramma":  # noqa
            genre.name = "Drama"
            genre.save()

    for actor in created_actors:
        if actor.last_name == "Klooney":  # noqa
            actor.last_name = "Clooney"
            actor.save()

        if actor.first_name == "Kianu":  # noqa
            actor.first_name = "Keanu"
            actor.last_name = "Reeves"
            actor.save()

    # Delete
    Genre.objects.get(name="Action").delete()

    actresses_scarlett = Actor.objects.filter(first_name="Scarlett")
    actresses_scarlett.delete()

    # Return
    actors_with_last_name_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return actors_with_last_name_smith
