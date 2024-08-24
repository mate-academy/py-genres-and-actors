import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def create_genre(data: list[str]) -> None:
    if isinstance(data[0], str):
        for row in data:
            Genre.objects.create(name=row)


def create_actor(data: list[tuple[str, str]]) -> None:
    if isinstance(data[0], tuple):
        for row in data:
            Actor.objects.create(first_name=row[0], last_name=row[1])


def update_genre(
        data: str | list[str],
        new_data: str | list[str]
) -> None:
    if isinstance(data, str) and isinstance(new_data, str):
        Genre.objects.filter(name=data).update(name=new_data)
    if isinstance(data, list) and isinstance(new_data, list):
        if isinstance(data[0], str):
            for i in range(len(data)):
                Genre.object.filter(name=data[i]).update(name=new_data[i])


def update_actor(
        data: tuple[str, str] | list[tuple[str, str]],
        new_data: tuple[str, str] | list[tuple[str, str]],
) -> None:
    if isinstance(data, tuple) and isinstance(new_data, tuple):
        Actor.objects.filter(
            first_name=data[0],
            last_name=data[1]
        ).update(
            first_name=new_data[0],
            last_name=new_data[1]
        )
    if isinstance(data, list) and isinstance(new_data, list):
        for data, new_data in zip(data, new_data):
            Actor.objects.filter(
                first_name=data[0],
                last_name=data[1]
            ).update(
                first_name=new_data[0],
                last_name=new_data[1]
            )


def delete_genre(
        name: str | list[str]
) -> None:
    if isinstance(name, str):
        Genre.objects.filter(name=name).delete()
    if isinstance(name, list):
        for row in name:
            Genre.objects.filter(name=row).delete()


def delete_actor(
        first_name: str | None = None,
        last_name: str | None = None
) -> None:
    if isinstance(first_name, str) and isinstance(last_name, str):
        Actor.objects.filter(
            first_name=first_name,
            last_name=last_name
        ).delete()
    elif isinstance(first_name, str) and last_name is None:
        Actor.objects.filter(first_name=first_name).delete()

    elif first_name is None and isinstance(last_name, str):
        Actor.objects.filter(last_name=last_name).delete()


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

    create_genre(genres)
    create_actor(actors)

    update_genre("Dramma", "Drama")
    update_actor(
        [("George", "Klooney"), ("Kianu", "Reaves")],
        [("George", "Clooney"), ("Keanu", "Reeves")]
    )

    delete_genre("Action")
    delete_actor(first_name="Scarlett")

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
