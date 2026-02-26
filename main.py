import init_django_orm  # noqa: F401

from db.models import Actor, Genre
from django.db.models import QuerySet

from typing import Any
from django.db.models import Model


def operate(
        model: type[Model],
        action: str,
        data: list[tuple] | list[Any],
) -> None:
    for item in data:
        if isinstance(item, tuple):
            getattr(model.objects, action)(
                first_name=item[0], last_name=item[1]
            )
        else:
            getattr(model.objects, action)(name=item)


def main() -> QuerySet:
    # Create
    genres = [("Western"), ("Action"), ("Dramma")]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    operate(Genre, "create", genres)
    operate(Actor, "create", actors)

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
