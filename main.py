import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",)
    ]

    # Create genres
    for genre in genres:
        Genre.objects.create(name=genre[0])

    # Update 'Dramma' to 'Drama'
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # List of tuples for actors
    actors = [
        ("George", "Klooney"),
        ("Keanu", "Reeves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    # Create actors
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Update specific actors
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # Delete specific genre and actresses
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return QuerySet of actors with last_name "Smith"
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
