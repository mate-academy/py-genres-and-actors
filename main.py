import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    # create
    genres = [
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma"),
    ]
    Genre.objects.bulk_create(genres)
    actors = [
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson"),
    ]
    Actor.objects.bulk_create(actors)
    # update
    updates = [
        (Genre.objects.filter(name="Dramma"), {"name": "Drama"}),
        (Actor.objects.filter(last_name="Klooney"), {"last_name": "Clooney"}),
        (Actor.objects.filter(first_name="Kianu", last_name="Reaves"),
         {"first_name": "Keanu", "last_name": "Reeves"}),
    ]

    for queryset, update_data in updates:
        queryset.update(**update_data)
    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
