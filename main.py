import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Create genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    # Create actors
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Update genre Dramma to Drama
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Update actors' details
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves")

    # Delete genre Action
    Genre.objects.filter(name="Action").delete()

    # Delete all actresses with first_name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # Query actors with last_name "Smith", ordered by first_name
    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    # Return QuerySet of actors with last_name "Smith"
    return smith_actors


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())
