import init_django_orm

from django.db.models import QuerySet
from db.models import Genre, Actor


def create_records() -> None:
    genres = [
        {"name": "Western"},
        {"name": "Action"},
        {"name": "Dramma"},
    ]

    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]

    for g in genres:
        Genre.objects.create(**g)

    for a in actors:
        Actor.objects.create(**a)


def update_records() -> None:
    updates = [
        (Genre.objects.filter(name="Dramma"), {"name": "Drama"}),
        (Actor.objects.filter(last_name="Klooney"), {"last_name": "Clooney"}),
        (
            Actor.objects.filter(first_name="Kianu", last_name="Reaves"),
            {"first_name": "Keanu", "last_name": "Reeves"},
        ),
    ]

    for qs, data in updates:
        qs.update(**data)


def delete_records() -> None:
    deletions = [
        Genre.objects.filter(name="Action"),
        Actor.objects.filter(first_name="Scarlett"),
    ]

    for qs in deletions:
        qs.delete()


def main() -> QuerySet:
    create_records()
    update_records()
    delete_records()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
