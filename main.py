import init_django_orm  # noqa: F401

from typing import Any

from db.models import Actor, Genre


def main() -> Any:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for genre in genres:
        Genre.objects.create(name=genre[0])

    for actor in actors:
        Actor.objects.create(
            first_name=actor[0],
            last_name=actor[1],
        )

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    george = Actor.objects.get(
        first_name="George",
        last_name="Klooney",
    )
    george.last_name = "Clooney"
    george.save()

    keanu = Actor.objects.get(
        first_name="Kianu",
        last_name="Reaves",
    )
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    Genre.objects.get(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
