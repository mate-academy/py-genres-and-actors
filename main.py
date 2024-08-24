from django.db.models import QuerySet
from db.models import Genre, Actor


def create_genres() -> None:
    genres = ["Western", "Action", "Dramma"]
    Genre.objects.bulk_create([Genre(name=genre) for genre in genres])

def create_actors() -> None:
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    Actor.objects.bulk_create(
        [
            Actor(first_name=first_name, last_name=last_name)
            for first_name, last_name in actors
        ]
    )

def update_genres() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")

def update_actors() -> None:
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        first_name="George",
        last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves")

def delete_genre() -> None:
    Genre.objects.filter(name="Action").delete()

def delete_scarlett_actors() -> None:
    Actor.objects.filter(first_name="Scarlett").delete()

def get_smith_actors() -> QuerySet:
    return Actor.objects.filter(last_name="Smith").order_by("first_name")

def main() -> QuerySet:
    create_genres()
    create_actors()
    update_genres()
    update_actors()
    delete_genre()
    delete_scarlett_actors()
    return get_smith_actors()