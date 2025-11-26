import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def create_records() -> None:
    genres = [
        "Western",
        "Action",
        "Dramma",
    ]

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for name in genres:
        Genre.objects.create(name=name)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_records() -> None:
    updates_genres = [
        ({"name": "Dramma"}, {"name": "Drama"}),
    ]

    updates_actors = [
        ({"last_name": "Klooney"}, {"last_name": "Clooney"}),
        (
            {"first_name": "Kianu", "last_name": "Reaves"},
            {"first_name": "Keanu", "last_name": "Reeves"},
        ),
    ]

    for query, data in updates_genres:
        Genre.objects.filter(**query).update(**data)

    for query, data in updates_actors:
        Actor.objects.filter(**query).update(**data)


def delete_records() -> None:
    deletions_genres = [
        {"name": "Action"},
    ]

    deletions_actors = [
        {"first_name": "Scarlett"},
    ]

    for genre in deletions_genres:
        Genre.objects.filter(**genre).delete()

    for actor in deletions_actors:
        Actor.objects.filter(**actor).delete()


def main() -> QuerySet:
    create_records()
    update_records()
    delete_records()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
