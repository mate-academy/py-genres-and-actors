import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    genres_to_add = ["Western", "Action", "Dramma"]
    for genre in genres_to_add:
        add_genre(genre)
    actors_to_add = [("George", "Klooney"), ("Kianu", "Reaves"),
                     ("Scarlett", "Keegan"), ("Will", "Smith"),
                     ("Jaden", "Smith"), ("Scarlett", "Johansson")]
    for first_name, second_name in actors_to_add:
        add_actor(first_name, second_name)
    update_genre("Dramma", "Drama")
    update_actor_last_name("George", "Klooney",
                           "Clooney")
    update_actor_first_name("Kianu", "Reaves", "Keanu")
    update_actor_last_name("Keanu", "Reaves", "Reeves")
    delete_genre("Action")
    delete_actors_by_first_name("Scarlett")
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def add_genre(genre: str) -> None:
    Genre.objects.create(
        name=genre,
    )


def add_actor(first_name: str, last_name: str) -> None:
    Actor.objects.create(
        first_name=first_name,
        last_name=last_name,
    )


def update_genre(old_name: str, new_name: str) -> None:
    Genre.objects.filter(
        name=old_name,
    ).update(name=new_name)


def update_actor_first_name(old_first_name: str,
                            old_last_name: str, new_first_name: str) -> None:
    Actor.objects.filter(
        first_name=old_first_name,
        last_name=old_last_name,
    ).update(first_name=new_first_name)


def update_actor_last_name(old_first_name: str,
                           old_last_name: str, new_last_name: str) -> None:
    Actor.objects.filter(
        first_name=old_first_name,
        last_name=old_last_name,
    ).update(last_name=new_last_name)


def delete_genre(genre_name: str) -> None:
    Genre.objects.filter(
        name=genre_name,
    ).delete()


def delete_actors_by_first_name(del_first_name: str) -> None:
    Actor.objects.filter(
        first_name=del_first_name,
    ).delete()
