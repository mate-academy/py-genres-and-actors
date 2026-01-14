import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Create genres
    genres = [("Western",), ("Action",), ("Dramma",)]
    for (genre_name,) in genres:
        Genre.objects.get_or_create(name=genre_name)

    # Create actors
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.get_or_create(first_name=first_name, last_name=last_name)

    # Update genre name "Dramma" to "Drama"
    try:
        genre = Genre.objects.get(name="Dramma")
        genre.name = "Drama"
        genre.save()
    except Genre.DoesNotExist:
        print("Genre 'Dramma' not found.")

    try:
        actor = Actor.objects.get(
            first_name="George", last_name="Klooney"
        )
        actor.last_name = "Clooney"
        actor.save()
    except Actor.DoesNotExist:
        print("Actor 'George Klooney' not found.")

    # Update actor Kianu Reaves to Keanu Reeves
    try:
        actor = Actor.objects.get(
            first_name="Kianu", last_name="Reaves"
        )
        actor.first_name = "Keanu"
        actor.last_name = "Reeves"
        actor.save()
    except Actor.DoesNotExist:
        print("Actor 'Kianu Reaves' not found.")

    # Delete the genre "Action"
    try:
        Genre.objects.filter(name="Action").delete()
    except Genre.DoesNotExist:
        print("Genre 'Action' not found.")

    # Delete all actresses with first_name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    )

    # Return or print the QuerySet
    print("Actors with last name 'Smith':")
    for actor in smith_actors:
        print(f"{actor.first_name} {actor.last_name}")

    return smith_actors
