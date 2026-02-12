import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for genre in genres:
        Genre.objects.create(
            name=genre
        )

    for actor in actors:
        Actor.objects.create(
            first_name=actor[0],
            last_name=actor[1]
        )

    genres_to_update = {
        "Dramma": "Drama"
    }
    actors_to_update = {
        ("George", "Klooney"): ("George", "Clooney"),
        ("Kianu", "Reaves"): ("Keanu", "Reeves")
    }

    for genre_key, genre_value in genres_to_update.items():
        Genre.objects.filter(
            name=genre_key
        ).update(name=genre_value)
    for actor_key, actor_value in actors_to_update.items():
        Actor.objects.filter(
            first_name=actor_key[0],
            last_name=actor_key[1]
        ).update(
            first_name=actor_value[0],
            last_name=actor_value[1]
        )

    genre_to_delete = ["Action"]
    actor_first_name_to_delete = "Scarlett"
    for genre in genre_to_delete:
        Genre.objects.filter(
            name=genre
        ).delete()

    Actor.objects.filter(
        first_name=actor_first_name_to_delete
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
