import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def genre_create(genres: list) -> None:
    Genre.objects.bulk_create(
        [Genre(name=genre) for genre in genres],
        ignore_conflicts=True
    )


def create_actors(actors: list[tuple[str, str]]) -> None:
    Actor.objects.bulk_create(
        [
            Actor(
                first_name=first_name,
                last_name=last_name
            ) for first_name, last_name in actors
        ],
        ignore_conflicts=True
    )


def update_name_genre(old_name: str, new_name: str) -> None:
    Genre.objects.filter(name=old_name).update(name=new_name)


def update_name_actor(
        old_first_name: str,
        new_first_name: str,
        old_last_name: str,
        new_last_name: str
) -> None:
    Actor.objects.filter(
        first_name=old_first_name,
        last_name=old_last_name
    ).update(
        first_name=new_first_name,
        last_name=new_last_name
    )


def delete_genre(name: str) -> None:
    Genre.objects.filter(name=name).delete()


def delete_actors(first_name: str) -> None:
    Actor.objects.filter(first_name=first_name).delete()


def get_actors_by_last_name(last_name: str) -> QuerySet:
    return Actor.objects.filter(last_name=last_name).order_by("first_name")


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    genre_create(genres)
    create_actors(actors)

    update_name_genre("Dramma", "Drama")
    update_name_actor("George", "George", "Klooney", "Clooney")
    update_name_actor("Kianu", "Keanu", "Reaves", "Reeves")

    delete_genre("Action")
    delete_actors("Scarlett")

    return get_actors_by_last_name("Smith")
