from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
    ]

    actress = [
        ("Scarlett", "Keegan"),
        ("Scarlett", "Johansson")
    ]

    #     1. Create
    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender="male"
        )

    for first_name, last_name in actress:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender="female"
        )

    #     2. Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    #     3. Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett", gender="female").delete()

    #     4. Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
