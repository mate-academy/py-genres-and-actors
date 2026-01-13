from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main() -> QuerySet:
    create_genres(("Western", "Action", "Dramma"))
    create_actors([("George", "Klooney"), ("Kianu", "Reaves"),
                   ("Scarlett", "Keegan"), ("Will", "Smith"),
                   ("Jaden", "Smith"), ("Scarlett", "Johansson")])
    update_genre_and_actors()
    delete_genre_and_actor()
    return actor_order()


def create_genres(genres_names: tuple) -> None:
    for name in genres_names:
        Genre.objects.create(name=name)


def create_actors(actors: list[tuple[str, str]]) -> None:
    for actor in actors:
        first_name, last_name = actor
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_genre_and_actors() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(first_name="George", last_name="Klooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))


def delete_genre_and_actor() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def actor_order() -> QuerySet:
    return (Actor.objects.filter(last_name="Smith")
            .order_by("first_name"))
