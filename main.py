import init_django_orm  # noqa F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres_data = ["Western", "Action", "Dramma"]

    # Creating genres
    for genre_name in genres_data:
        Genre.objects.create(name=genre_name)

    actors_data = [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Will", "Smith"),
        ("Jaden", "Smith")
    ]

    # Creating actors
    for first_name, last_name in actors_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Updating genre names
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Updating actor names
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(
        first_name="Keanu", last_name="Reeves"
    )

    # Deleting the genre "Action"
    Genre.objects.filter(name="Action").delete()

    # Deleting actors with the first name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # Returning actors with the last name "Smith"
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
