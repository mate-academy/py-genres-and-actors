import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors_names = ["George", "Kianu", "Scarlett",
                    "Will", "Jaden", "Scarlett"]
    actors_surnames = ["Klooney", "Reaves", "Keegan",
                       "Smith", "Smith", "Johansson"]

    for actors_name, actors_surname in zip(actors_names, actors_surnames):
        Actor.objects.create(first_name=actors_name, last_name=actors_surname)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
