import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    genres = [
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma"),
    ]
    Genre.objects.bulk_create(genres)
    print(Genre.objects.all())

    actors = [
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson"),
    ]
    Actor.objects.bulk_create(actors)
    print(Actor.objects.all())

    # Update genre
    Genre.objects.filter(name="Dramma").update(name="Drama")

    for actor in Actor.objects.filter(last_name="Klooney"):
        actor.last_name = "Clooney"
        actor.save()

    for actor in Actor.objects.filter(
            first_name="Kianu",
            last_name="Reaves"
    ):
        actor.first_name = "Keanu"
        actor.last_name = "Reeves"
        actor.save()

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors
