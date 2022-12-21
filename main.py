import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre = [
        "Western",
        "Action",
        "Dramma"
    ]
    actor = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for genre_name in genre:
        Genre.object.create(
            name=genre_name
        )

    for add_first_name, add_last_name in actor:
        Actor.object.create(
            first_name=add_first_name,
            last_name=add_last_name
        )
    Genre.object.filter(name="Dramma").update("Drama")
    Actor.object.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        first_name="George",
        last_name="Clooney"
    )
    Actor.object.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.object.filter(name="Action").delete()
    Actor.object.filter(first_name="Scarlett").delete()

    return Actor.object.filter(last_name="Smith").order_by()
