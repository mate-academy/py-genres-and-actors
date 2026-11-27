from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
<<<<<<< HEAD
    # Create genres
=======
>>>>>>> fade632385ba7e11040e85863946430d895e8c69
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

<<<<<<< HEAD
    # Create actors and actresses
=======
>>>>>>> fade632385ba7e11040e85863946430d895e8c69
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

<<<<<<< HEAD
    # Update genre
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Update actors
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # Delete genre
    Genre.objects.filter(name="Action").delete()

    # Delete all actresses named Scarlett
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return actors with last_name Smith, ordered by first_name
=======
    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

>>>>>>> fade632385ba7e11040e85863946430d895e8c69
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
