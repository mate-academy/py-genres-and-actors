import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    # create
    genres = ["Western", "Action", "Dramma"]
    actors_and_actresses = {"George": "Klooney",
                            "Kianu": "Reaves",
                            "Scarlett": "Keegan",
                            "Will ": "Smith",
                            "Jaden": "Smith",
                            "Scarlett": "Johansson"}

    for i in genres:
        Genre.objects.create(i)

    for key, value in actors_and_actresses:
        Actor.objects.create(key, value)

    # Update

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # Delete

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Final return

    return Actor.objects.filter(last_name="Smith").order_by("last_name")
