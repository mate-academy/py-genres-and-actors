import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

genre_objects = [
    Genre(name="Western"),
    Genre(name="Action"),
    Genre(name="Dramma"),
]
actors_objects = [
    Actor(first_name="George", last_name="Klooney"),
    Actor(first_name="Kianu", last_name="Reaves"),
    Actor(first_name="Scarlett", last_name="Keegan"),
    Actor(first_name="Will", last_name="Smith"),
    Actor(first_name="Jaden", last_name="Smith"),
    Actor(first_name="Scarlett", last_name="Johansson"),
]


def main() -> QuerySet:
    Genre.objects.bulk_create(genre_objects)
    Actor.objects.bulk_create(actors_objects)
    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney",
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(
        name="Action",
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()
    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors


if __name__ == "__main__":
    main()
