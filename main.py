import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(genre)

    for actor_name in ["George Klooney",
                       "Kianu Reaves",
                       "Scarlett Keegan",
                       "Will Smith",
                       "Jaden Smith",
                       "Scarlet Johansson"]:
        Actor.objects.create(actor_name.split(" "))

    Genre.objects.update(name="Dramma", new_name="Drama")

    Actor.objects.update(last_name="Klooney", new_name="Clooney")
    Actor.objects.update(first_name="Kianu", new_name="Keanu")
    Actor.objects.update(last_name="Reaves", new_name="Reeves")

    Genre.objects.delete("Action")
    Actor.objects.delete(first_name="Scarlett")

    return Actor.objects.filter(last_name="Smith").order_by('last_name')

