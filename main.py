import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def crud_for_genres() -> QuerySet:
    # Create a new genres in table:
    genres = ["Western", "Action", "Dramma"]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    # Update an existing genre name to a new:
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Deleting an existing genre from table:
    Genre.objects.filter(name="Action").delete()

    # Read data from table:
    return Genre.objects.all()


def crud_for_actors() -> QuerySet:
    # Create new actors inputs in table:
    actors = [
        {
            "first_name": "George", "last_name": "Klooney"
        },
        {
            "first_name": "Kianu", "last_name": "Reaves"
        },
        {
            "first_name": "Scarlett", "last_name": "Keegan"
        },
        {
            "first_name": "Will", "last_name": "Smith"
        },
        {
            "first_name": "Jaden", "last_name": "Smith"
        },
        {
            "first_name": "Scarlett", "last_name": "Johansson"
        }
    ]
    for actor in actors:
        Actor.objects.create(**actor)

    # Update an existing actors' attributes:
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # Deleting an existing actor's attribute
    Actor.objects.filter(first_name="Scarlett").delete()

    # Read data from table
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def main() -> QuerySet:
    crud_for_genres()
    return crud_for_actors()
