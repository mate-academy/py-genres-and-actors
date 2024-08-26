import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def create_genres(genres: list[str]) -> None:
    for genre in genres:
        Genre.objects.create(name=genre)


def create_actors(actors: list[tuple[str, str]]) -> None:
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_genres(updates: dict[str, str]) -> None:
    for old_name, new_name in updates.items():
        Genre.objects.filter(name=old_name).update(name=new_name)


def update_actors(
        updates: list[
            tuple[dict[str, str], dict[str, str]]
        ]
) -> None:
    for filter_kwargs, update_kwargs in updates:
        Actor.objects.filter(**filter_kwargs).update(**update_kwargs)


def delete_genres(genre_names: list[str]) -> None:
    for name in genre_names:
        Genre.objects.filter(name=name).delete()


def delete_actors(filter_kwargs: dict[str, str]) -> None:
    Actor.objects.filter(**filter_kwargs).delete()


def main() -> QuerySet:
    create_genres(["Western", "Action", "Dramma"])

    create_actors([
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ])

    update_genres({"Dramma": "Drama"})

    update_actors([
        (
            {
                "first_name": "George",
                "last_name": "Klooney"
            },
            {
                "last_name": "Clooney"}),
        (
            {
                "first_name": "Kianu",
                "last_name": "Reaves"
            },
            {
                "first_name": "Keanu",
                "last_name": "Reeves"
            }
        ),
    ])

    delete_genres(["Action"])
    delete_actors({"first_name": "Scarlett"})

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
