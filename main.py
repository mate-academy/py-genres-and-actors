import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def create_actors_and_genres() -> None:
    genres = ["Western", "Action", "Dramma"]
    Genre.objects.bulk_create([Genre(name=genre) for genre in genres])
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


def update_actors_and_genres() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")

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


def delete_actors_and_genres() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def get_() -> QuerySet:
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def main() -> QuerySet:
    create_actors_and_genres()
    update_actors_and_genres()
    delete_actors_and_genres()
    return get_()
