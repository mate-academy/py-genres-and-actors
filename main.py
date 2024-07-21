import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    create_genres(("Western", "Action", "Dramma"))
    create_actors({
        "actor1": {
            "first_name": "George",
            "last_name": "Klooney"
        },

        "actor2": {
            "first_name": "Kianu",
            "last_name": "Reaves"
        },

        "actress1": {
            "first_name": "Scarlett",
            "last_name": "Keegan"
        },

        "actor3": {
            "first_name": "Will",
            "last_name": "Smith"
        },

        "actor4": {
            "first_name": "Jaden",
            "last_name": "Smith"
        },

        "actress2": {
            "first_name": "Scarlett",
            "last_name": "Johansson"
        },
    })

    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")

    (Actor.objects.filter(first_name="George", last_name="Klooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))

    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def create_genres(genres_names: tuple) -> None:
    for name in genres_names:
        Genre.objects.create(name=name)


def create_actors(actors: dict) -> None:
    for actor in actors.values():
        Actor.objects.create(first_name=actor["first_name"],
                             last_name=actor["last_name"])
