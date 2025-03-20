import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.bulk_create([
        Genre(genre="Western"),
        Genre(genre="Action"),
        Genre(genre="Dramma"),
    ])
    Genre.objects.filter(genre="Dramma").update(genre="Drama")
    Genre.objects.filter(genre="Action").delete()

    Actor.objects.bulk_create([
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson"),
    ])

    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Smith")
    Actor.objects.filter(first_name="Scarlett").delete()
    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors


if __name__ == "__main__":
    main()
