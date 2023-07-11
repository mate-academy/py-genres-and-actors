from db.models import Actor, Genre
import init_django_orm  # noqa: F401

from django.db.models import QuerySet


def main() -> QuerySet:
    genres = [Genre(name=genre) for genre in ["Western", "Action", "Dramma"]]
    actors = [
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson")
    ]
    Genre.objects.bulk_create(genres)
    Actor.objects.bulk_create(actors)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney",
        first_name="George"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        last_name="Reaves",
        first_name="Kianu"
    ).update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
