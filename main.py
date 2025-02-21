import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)
    for actor_name in ["George Klooney",
                       "Kianu Reaves",
                       "Scarlett Keegan",
                       "Will Smith",
                       "Jaden Smith",
                       "Scarlet Johansson"]:
        name_parts = actor_name.split(" ")
        Actor.objects.create(first_name=name_parts[0], last_name=name_parts[1])
    Genre.objects.filter(name="Dramma").update(new_name="Drama")
    Actor.objects.filter(last_name="Klooney").update(name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("last_name")
