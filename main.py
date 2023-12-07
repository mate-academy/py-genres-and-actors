from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        Genre.objects.create(name="Western"),
        Genre.objects.create(name="Action"),
        Genre.objects.create(name="Drama"),
    ]

    actors = [
        Actor.objects.create(first_name="George", last_name="Clooney"),
        Actor.objects.create(first_name="Keanu", last_name="Reeves"),
        Actor.objects.create(first_name="Scarlett", last_name="Keegan"),
        Actor.objects.create(first_name="Will", last_name="Smith"),
        Actor.objects.create(first_name="Jaden", last_name="Smith"),
        Actor.objects.create(first_name="Scarlett", last_name="Johansson"),
    ]

    genres[2].name = "Drama"
    actors[0].last_name = "Clooney"
    actors[1].first_name = "Keanu"
    actors[1].last_name = "Reeves"

    for obj in genres + actors:
        obj.save()

    genres[1].delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(
        last_name="Smith").order_by("first_name")
    for actor in smith_actors:
        print(f"{actor.first_name} {actor.last_name}")

    return smith_actors
