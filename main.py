import init_django_orm  # noqa: F401
from db.models import Actor, Genre
from django.db.models import QuerySet


def main() -> QuerySet:
    genres = [
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma"),
    ]
    actors = [
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson"),
    ]

    Genre.objects.bulk_create(genres)
    Actor.objects.bulk_create(actors)

    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()

    george_klooney = Actor.objects.get(
        first_name="George", last_name="Klooney")
    george_klooney.last_name = "Clooney"
    george_klooney.save()

    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    action = Genre.objects.get(name="Action")
    action.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    smitt = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smitt
