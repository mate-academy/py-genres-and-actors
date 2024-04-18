from typing import Type

from django.db.models import QuerySet, Model

import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def create(model: Type[Model], values_to_create: dict) -> None:
    model.objects.create(**values_to_create)


def update(
        model: Type[Model],
        filter_conditions: dict,
        update_values: dict
) -> None:
    model.objects.filter(**filter_conditions).update(**update_values)


def delete(model: Type[Model], filter_conditions: dict) -> None:
    model.objects.filter(
        **filter_conditions,
    ).delete()


def get_by_filter(model: Type[Model], filter_conditions: dict) -> QuerySet:
    return model.objects.filter(**filter_conditions)


def main() -> QuerySet:
    for genre in [{"name": "Western"}, {"name": "Action"}, {"name": "Dramma"}]:
        create(Genre, genre)

    actors = [
        {
            "first_name": "George",
            "last_name": "Klooney"
        },
        {
            "first_name": "Kianu",
            "last_name": "Reaves"
        },
        {
            "first_name": "Scarlett",
            "last_name": "Keegan"
        },
        {
            "first_name": "Will",
            "last_name": "Smith"
        },
        {
            "first_name": "Jaden",
            "last_name": "Smith"
        },
        {
            "first_name": "Scarlett",
            "last_name": "Johansson"
        },
    ]
    for actor in actors:
        create(Actor, actor)

    update(Genre, {"name": "Dramma"}, {"name": "Drama"})
    update(Actor, {"last_name": "Klooney"}, {"last_name": "Clooney"})
    update(
        Actor,
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Keanu", "last_name": "Reeves"})

    delete(Genre, {"name": "Action"})
    delete(Actor, {"first_name": "Scarlett"})

    return get_by_filter(Actor, {"last_name": "Smith"}).order_by("first_name")
