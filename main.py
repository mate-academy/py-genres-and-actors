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
    Genre.object.bulk_create(to_create_genres)

    to_create_actors = [
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson")
    ]
    Actor.object.bulk_create(to_create_actors)

    # Update

    Genre.object.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.object.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.object.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(last_name="Reeves", first_name="Keanu")

    # Delete

    Genre.object.filter(
        name="Action"
    ).delete()

    Actor.object.filter(
        first_name="Scarlett"
    ).delete()

    # Get(Return)

    Actor.object.get(
        last_name="Smith"
    ).order_by()
