import init_django_orm  # noqa: F401

from django.db.models import QuerySet  # noqa: F401
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [("Western",), ("Action",), ("Dramma",)]
    for (genre_name,) in genres:
        Genre.objects.create(name=genre_name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Scarlett", "Johansson"),
        ("Jaden", "Smith"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    actor = Actor.objects.get(first_name="George", last_name="Klooney")
    actor.first_name = "George"
    actor.last_name = "Clooney"
    actor.save()

    actor2 = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor2.first_name = "Keanu"
    actor2.last_name = "Reeves"
    actor2.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
