import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # create
    genres_names_to_create = ["Western", "Action", "Dramma"]
    for genre_name in genres_names_to_create:
        Genre.objects.create(
            name=genre_name
        )

    input_actors_fullnames_to_create = [
        "George Klooney", "Kianu Reaves", "Scarlett Keegan",
        "Will Smith", "Jaden Smith", "Scarlett Johansson"
    ]
    actors_names_to_create = (
        (actor_name.split()[0], actor_name.split()[1])
        for actor_name
        in input_actors_fullnames_to_create
    )
    for first_name, last_name in actors_names_to_create:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
