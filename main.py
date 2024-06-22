import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    first_name = ["George", "Kianu", "Scarlett", "Will", "Jaden", "Scarlett"]
    last_name = ["Klooney", "Reaves", "Keegan", "Smith", "Smith", "Johansson"]
    if len(first_name) != len(last_name):
        raise ValueError("Value error")
    for i in range(len(first_name)):
        Actor.objects.create(first_name=first_name[i], last_name=last_name[i])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George",
                         last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu",
                         last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    actors_name_smith = Actor.objects.filter(
        last_name="Smith").order_by("first_name")
    return actors_name_smith
