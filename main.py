import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor
from to_add import genres, actors


def main() -> QuerySet:

    Actor.objects.all().delete()
    Genre.objects.all().delete()
    # Create
    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return
    smith_filter = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return smith_filter
