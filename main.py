import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    list_of_genre = ["Western", "Action", "Dramma"]
    list_of_actor = ["George Klooney", "Scarlett Johansson", "Kianu Reaves",
                     "Scarlett Keegan", "Will Smith", "Jaden Smith"]

    Genre.objects.bulk_create([
        Genre(name=genre)
        for genre in list_of_genre
    ])

    Actor.objects.bulk_create([
        Actor(first_name=actor.split()[0],
              last_name="".join(actor.split()[1:]))
        for actor in list_of_actor
    ])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")
