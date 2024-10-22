from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import Actor, Genre


def main() -> QuerySet:
    list_of_genre_name = ["Western", "Action", "Dramma"]
    dict_actors = [
        {"first_name": "George", "last_name": "Clooney"},
        {"first_name": "Keanu", "last_name": "Reeves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]

    # Create GENRE with list genre

    for genre_name in list_of_genre_name:
        Genre.objects.create(name=genre_name)

    # Create ACTORS with dict actors

    for actor in dict_actors:
        Actor.objects.create(**actor)

    # UPDATE genre Dramma, set name to "Drama"
    # actor George Klooney, set last_name to "Clooney"
    # actor Kianu Reaves, set first_name to "Keanu" and last_name to "Reeves"

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reeves").update(first_name="Keanu")

    # DELETE
    # genre Action
    # all actresses with the first_name "Scarlett"

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return:
    # QuerySet of actors with last_name "Smith" and ordered by first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
