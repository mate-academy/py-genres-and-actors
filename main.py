import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def create(data: list[str] | list[tuple[str, str]]) -> None:
    if isinstance(data[0], str):
        for row in data:
            Genre.objects.create(name=row)
    if isinstance(data[0], tuple):
        for row in data:
            first_name, last_name = row
            Actor.objects.create(first_name=first_name, last_name=last_name)


def _update_genre(
        name: str,
        new_name: str
) -> None:
    Genre.objects.filter(name=name).update(name=new_name)


def _update_actor(
        fl_name: tuple[str, str],
        new_fl_name: tuple[str, str]
) -> None:
    first_name, last_name = fl_name
    new_first_name, new_last_name = new_fl_name
    Actor.objects.filter(
        first_name=first_name,
        last_name=last_name
    ).update(
        first_name=new_first_name,
        last_name=new_last_name
    )


def update(
        data: list[str | tuple[str, str]] | str | tuple[str, str],
        new_data: list[str | tuple[str, str]] | str | tuple[str, str]
) -> None:
    if isinstance(data, str) and isinstance(new_data, str):
        _update_genre(data, new_data)
    if isinstance(data, tuple) and isinstance(new_data, tuple):
        _update_actor(data, new_data)
    if isinstance(data, list) and isinstance(new_data, list):
        if isinstance(data[0], str):
            for i in range(len(data)):
                _update_genre(data[i], new_data[i])
        if isinstance(data[0], tuple):
            for i in range(len(data)):
                _update_actor(data[i], new_data[i])


def delete(
        genre_name: str | None = None,
        actor_first_name: str | None = None,
        actor_last_name: str | None = None,
) -> None:
    if genre_name is not None:
        Genre.objects.filter(name=genre_name).delete()
    if actor_first_name is not None:
        Actor.objects.filter(first_name=actor_first_name).delete()
    if actor_last_name is not None:
        Actor.objects.filter(last_name=actor_last_name).delete()


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

    create(genres)
    create(actors)

    update("Dramma", "Drama")
    update(
        [("George", "Klooney"), ("Kianu", "Reaves")],
        [("George", "Clooney"), ("Keanu", "Reeves")]
    )

    delete(genre_name="Action")
    delete(actor_first_name="Scarlett")

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
