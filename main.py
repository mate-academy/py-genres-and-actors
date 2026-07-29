from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet[Actor]:
    # Create genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    # Create actors
    Actor.objects.create(
        first_name="George",
        last_name="Klooney",
    )
    Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )

    # Update genre
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Update George Klooney
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney",
    ).update(last_name="Clooney")

    # Update Kianu Reaves
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(
        first_name="Keanu",
        last_name="Reeves",
    )

    # Delete Action genre
    Genre.objects.filter(name="Action").delete()

    # Delete all actors named Scarlett
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return Smith actors ordered by first name
    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
