import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = [
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma")
    ]
    Genre.objects.bulk_create(genres)

    actors = [
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson")
    ]

    Actor.objects.bulk_create(actors)

    genre_dramma = Genre.objects.get(name="Dramma")
    genre_dramma.name = "Drama"

    actor_george_klooney = Actor.objects.get(first_name="George",
                                             last_name="Klooney")
    actor_george_klooney.last_name = "Clooney"

    actor_kianu = Actor.objects.get(first_name="Kianu",
                                    last_name="Reaves")
    actor_kianu.first_name, actor_kianu.last_name = "Keanu", "Reeves"

    action = Genre.objects.get(name="Action")
    action.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    all_actors = Actor.objects.all()
    filtered_actors = all_actors.objects.filter(last_name="Smith")
    ordered_actors = filtered_actors.objects.order_by('-first_name')
    return ordered_actors
