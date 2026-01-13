import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:

    # Create

    to_create_genres = [
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma")
    ]
    Genre.objects.bulk_create(to_create_genres)

    to_create_actors = [
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson")
    ]
    Actor.objects.bulk_create(to_create_actors)

    # Update

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(last_name="Reeves", first_name="Keanu")

    # Delete

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    # Get(Return)

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
