import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Create genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    # Create actors and actresses
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")  # Actress
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Update "Dramma" genre to "Drama"
    Genre.objects.filter(name="Dramma").update(
        name="Drama"
    )

    # Update "George Klooney" to "George Clooney"
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")

    # Update "Kianu Reaves" to "Keanu Reeves"
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # Delete "Action" genre
    Genre.objects.filter(name="Action").delete()

    # Delete all actresses with the first name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # Query actors with last name "Smith" ordered by first name
    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return smith_actors


if __name__ == "__main__":
    smith_actors = main()
    for actor in smith_actors:
        print(actor)
