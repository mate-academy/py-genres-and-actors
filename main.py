import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_names = ["Western", "Action", "Dramma"]
    for genre_name in genre_names:
        Genre.objects.create(
            name=genre_name
        )

    actors = ["George Klooney", "Kianu Reaves", "Scarlett Keegan",
              "Will Smith", "Jaden Smith", "Scarlett Johansson"]

    for actor in actors:
        first_name, last_name = actor.split()
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )
    genre_drama = Genre.objects.get(name="Dramma")
    genre_drama.name = "Drama"
    genre_drama.save()

    clooney = Actor.objects.get(first_name="George", last_name="Klooney")
    clooney.last_name = "Clooney"
    clooney.save()

    keanu_reeves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    keanu_reeves.first_name, keanu_reeves.last_name = ("Keanu", "Reeves")
    keanu_reeves.save()

    action = Genre.objects.get(name="Action")
    action.delete()

    scarlets = Actor.objects.filter(first_name="Scarlett")
    scarlets.delete()

    smiths = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return smiths
