import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [("Western",), ("Action",), ("Dramma",)]
    for name, in genres:
        Genre.objects.create(name=name)
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    genre = Actor.objects.get(last_name="Klooney")
    genre.last_name = "Clooney"
    genre.save()

    genre = Actor.objects.get(first_name="Kianu")
    genre.first_name = "Keanu"
    genre.last_name = "Reeves"
    genre.save()

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
