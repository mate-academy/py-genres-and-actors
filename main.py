import init_django_orm  # noqa: F401

from db.models import Actor, Genre
from django.db.models import QuerySet

from typing import Optional, Any
from django.db.models import Model


def operate(
        model: type[Model],
        action: str,
        data: list[dict] | list[Any],
        column: Optional[str] = None
) -> None:
    for item in data:
        if isinstance(item, dict):
            getattr(model.objects, action)(**item)
        else:
            if column is None:
                raise ValueError(
                    "Column name must be provided for single-value data"
                )
            getattr(model.objects, action)(**{column: item})


def main() -> QuerySet:
    # Create
    genres = ["Western", "Action", "Dramma"]
    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]
    operate(Genre, "create", genres, column="name")
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
