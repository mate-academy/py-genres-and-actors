from collections import namedtuple  # noqa: F401

import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)
    # Genre.objects.create(name="Western")
    # Genre.objects.create(name="Action")
    # Genre.objects.create(name="Dramma")
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_n, last_n in actors:
        Actor.objects.create(
            first_name=first_n, last_name=last_n
        )
    # Actor.objects.create(first_name="George", last_name= "Klooney")
    # Actor.objects.create(first_name="Kianu", last_name= "Reaves")
    # Actor.objects.create(first_name="Scarlett", last_name= "Keegan")
    # Actor.objects.create(first_name="Will", last_name= "Smith")
    # Actor.objects.create(first_name="Jaden", last_name= "Smith")
    # Actor.objects.create(first_name="Scarlett", last_name= "Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.all().filter(last_name="Smith").order_by("first_name")
