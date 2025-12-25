import init_django_orm  # noqa: F401

from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:

    # Create elements
    list_of_genres = ["Western", "Action", "Dramma"]
    for i in list_of_genres:
        Genre.objects.create(name=i)

    actors_name_list = [
        "George", "Kianu", "Scarlett", "Will", "Jaden", "Scarlett"
    ]
    actors_surname_list = [
        "Klooney", "Reaves", "Keegan", "Smith", "Smith", "Johansson"
    ]
    for i in range(len(actors_name_list)):
        Actor.objects.create(
            first_name=actors_name_list[i],
            last_name=actors_surname_list[i]
        )

    # Update elements
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # Delete elements
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return realization
    actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return actors
