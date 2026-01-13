import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def create(data: list) -> None:
    if isinstance(data[0], str):
        for genre in data:
            Genre.objects.create(name=genre)
    else:
        for first_name, last_name in data:
            Actor.objects.create(
                first_name=first_name,
                last_name=last_name
            )


def update(data: list) -> None:
    if isinstance(data[0], str):
        Genre.objects.filter(
            name="Dramma"
        ).update(
            name="Drama"
        )
    else:
        Actor.objects.filter(
            last_name="Klooney"
        ).update(
            last_name="Clooney"
        )
        Actor.objects.filter(
            first_name="Kianu"
        ).update(
            first_name="Keanu",
            last_name="Reeves"
        )


def delete(data: list) -> None:
    if isinstance(data[0], str):
        Genre.objects.filter(
            name="Action"
        ).delete()
    else:
        Actor.objects.filter(
            first_name="Scarlett"
        ).delete()


def sort() -> QuerySet:
    sorted_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return sorted_actors


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]

    create(genres)

    names_of_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    create(names_of_actors)

    update(genres)
    update(names_of_actors)

    delete(genres)
    delete(names_of_actors)

    return sort()
