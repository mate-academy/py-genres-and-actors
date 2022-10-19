import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    actor1 = Actor.objects.get(
        first_name="George", last_name="Klooney"
    )
    actor1.last_name = "Clooney"
    actor1.save()

    actor2 = Actor.objects.get(
        first_name="Kianu", last_name="Reaves"
    )
    actor2.first_name = "Keanu"
    actor2.last_name = "Reeves"
    actor2.save()

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
