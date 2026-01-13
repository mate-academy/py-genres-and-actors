import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def create_genres(genres: list) -> None:
    for genre in genres:
        Genre.objects.create(name=genre)


def create_actors(actors: list) -> None:
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_genres_and_actors() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")


def delete_genre_and_actor() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    create_actors(actors)
    create_genres(genres)
    update_genres_and_actors()
    delete_genre_and_actor()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
