import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:

    # Create
    Genre.objects.create(genre="Western")
    Genre.objects.create(genre="Action")
    Genre.objects.create(genre="Dramma")

    Actor.objects.create(
        first_name="George",
        last_name="Klooney"
    )
    Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves"
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan"
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith"
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith"
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson"
    )

    # Update
    Genre.objects.filter(
        genre="Dramma"
    ).update(genre="Drama")

    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # Delete
    Genre.objects.filter(
        genre="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    # Return
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
