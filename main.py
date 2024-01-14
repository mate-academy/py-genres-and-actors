from typing import List
from django.db.models import QuerySet
from db.models import Genre, Actor


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
    genre_names = ["Western", "Action", "Drama"]
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
    created_genres[2].name = "Drama"
    created_genres[2].save()

    created_actors[0].last_name = "Clooney"
    created_actors[0].save()

    created_actors[1].first_name = "Keanu"
    created_actors[1].last_name = "Reeves"
    created_actors[1].save()

    # Delete
    Genre.objects.get(name="Action").delete()

    actresses_scarlett = Actor.objects.filter(first_name="Scarlett")
    actresses_scarlett.delete()

    # Return
    actors_with_last_name_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return actors_with_last_name_smith
