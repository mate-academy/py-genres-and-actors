from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    fill_tables(genres, actors)

    update_genre(name_to_seek="Dramma", new_name="Drama")

    update_actors(
        first_name_to_seek="George",
        last_name_to_seek="Klooney",
        new_last_name="Clooney"
    )
    update_actors(
        first_name_to_seek="Kianu",
        last_name_to_seek="Reaves",
        new_first_name="Keanu",
        new_last_name="Reeves"
    )

    delete_genre("Action")

    delete_actors(first_name_to_seek="Scarlett")

    return find_and_sort_actors(
        last_name_to_seek="Smith", order_by="first_name"
    )


def fill_tables(genres: list[str], actors: list[tuple[str, str]]) -> None:
    for genre in genres:
        Genre.objects.create(name=genre)
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_genre(name_to_seek: str, new_name: str) -> None:
    Genre.objects.filter(name=name_to_seek).update(name=new_name)


def delete_genre(genre_name: str) -> None:
    Genre.objects.get(name=genre_name).delete()


def update_actors(
    first_name_to_seek: str | None = None,
    last_name_to_seek: str | None = None,
    new_first_name: str | None = None,
    new_last_name: str | None = None
) -> None:
    found_actors = find_actors(
        first_name_to_seek=first_name_to_seek,
        last_name_to_seek=last_name_to_seek
    )
    new_data = {}

    if isinstance(new_first_name, str):
        new_data["first_name"] = new_first_name
    if isinstance(new_last_name, str):
        new_data["last_name"] = new_last_name

    found_actors.update(**new_data)


def delete_actors(
    first_name_to_seek: str | None = None,
    last_name_to_seek: str | None = None
) -> None:
    find_actors(first_name_to_seek, last_name_to_seek).delete()


def find_and_sort_actors(
    first_name_to_seek: str | None = None,
    last_name_to_seek: str | None = None,
    order_by: str | None = None
) -> QuerySet:
    return find_actors(
        first_name_to_seek,
        last_name_to_seek
    ).order_by(order_by)


def find_actors(
    first_name_to_seek: str | None = None,
    last_name_to_seek: str | None = None,
) -> QuerySet:
    filter_ = {}

    if isinstance(first_name_to_seek, str):
        filter_["first_name"] = first_name_to_seek
    if isinstance(last_name_to_seek, str):
        filter_["last_name"] = last_name_to_seek

    return Actor.objects.filter(**filter_)


if __name__ == "__main__":
    main()
