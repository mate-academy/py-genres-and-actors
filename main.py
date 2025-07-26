import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma")
    ]
    actors = [
        Actor(first_name="George",
              last_name="Klooney"),
        Actor(first_name="Kianu",
              last_name="Reaves"),
        Actor(first_name="Scarlett",
              last_name="Keegan"),
        Actor(first_name="Will",
              last_name="Smith"),
        Actor(first_name="Jaden",
              last_name="Smith"),
        Actor(first_name="Scarlett",
              last_name="Johansson")
    ]
    Genre.objects.bulk_create(genres)
    Actor.objects.bulk_create(actors)

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    update_actors = list(Actor.objects.filter(id__in=[1, 2, 3]))

    update_actors[0].last_name = "Clooney"
    update_actors[1].first_name = "Keanu"
    update_actors[1].last_name = "Reeves"

    Actor.objects.bulk_update(update_actors, ["first_name", "last_name"])

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
