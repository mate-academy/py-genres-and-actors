from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [("Western",), ("Action",), ("Drama",)]
    for (name,) in genres:
        Genre.objects.create(name=name)

    actors = [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
