from calendar import firstweekday

import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actors, Genre


def main() -> QuerySet:

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for actor in actors:
        Actors.objects.create(
            first_name = actor[0],
            last_name = actor[1]
        )

    genres = [
        "Western",
        "Action",
        "Dramma"
    ]

    for genre in genres:
        Genre.objects.create(name=genre)

    Genre.objects.filter(name = "Dramma").update(name = "Drama")
    Actors.objects.filter(last_name = "Klooney").update(last_name = "Clooney")
    Actors.objects.filter(last_name = "Reaves").update(first_name = "Keanu", last_name = "Reeves")

    Genre.objects.filter(name = "Action").delete()
    Actors.objects.filter(first_name = "Scarlett").delete()

    query_set = Actors.objects.get(last_name = "Smith").order_by(first_name)
    return query_set
