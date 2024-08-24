from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main() -> QuerySet:
    create_genres(("Western", "Action", "Dramma"))
    create_actors([("George", "Klooney"), ("Kianu", "Reaves"),
                   ("Scarlett", "Keegan"), ("Will", "Smith"),
                   ("Jaden", "Smith"), ("Scarlett", "Johansson")])

    update_genre("Dramma", "Drama")
    update_actor(
        first_name_to_find="George",
        last_name_to_find="Klooney",
        last_name_to_update="Clooney"
    )
    update_actor(
        first_name_to_find="Kianu",
        last_name_to_find="Reaves",
        first_name_to_update="Keanu",
        last_name_to_update="Reeves"
    )

    # delete
    delete_genre("Action")
    delete_actor(first_name="Scarlett")

    return actor_order("first_name", last_name="Smith")


def create_genres(genres_names: tuple) -> None:
    for name in genres_names:
        Genre.objects.create(name=name)


def create_actors(actors: list[tuple[str, str]]) -> None:
    for actor in actors:
        first_name, last_name = actor
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_genre(name_to_find: str, name_to_update: str) -> None:
    Genre.objects.filter(name=name_to_find).update(name=name_to_update)


def update_actor(
        first_name_to_find: str,
        last_name_to_find: str = None,
        first_name_to_update: str = None,
        last_name_to_update: str = None
) -> None:
    actors = Actor.objects.filter(first_name=first_name_to_find)
    if last_name_to_find is not None:
        actors = actors.filter(last_name=last_name_to_find)

    if last_name_to_update and first_name_to_update:
        actors.update(
            first_name=first_name_to_update,
            last_name=last_name_to_update
        )
    elif last_name_to_find is None:
        actors.update(first_name=first_name_to_find)
    else:
        actors.update(last_name=last_name_to_update)


def delete_genre(name_to_delete: str) -> None:
    Genre.objects.filter(name=name_to_delete).delete()


def delete_actor(**names_to_delete) -> None:
    Actor.objects.filter(**names_to_delete).delete()


def actor_order(*order_by, **filter_kwargs) -> QuerySet:
    return Actor.objects.filter(**filter_kwargs).order_by(*order_by)


if __name__ == "__main__":
    print(main())
