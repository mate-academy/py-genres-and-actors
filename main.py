import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_list = ["Western", "Action", "Dramma"]
    actors_list = [("George", "Klooney"),
                   ("Kianu", "Reaves"),
                   ("Scarlett", "Keegan"),
                   ("Will", "Smith"),
                   ("Jaden", "Smith"),
                   ("Scarlett", "Johansson")
                   ]
    for genre in genre_list:
        Genre.objects.create(
            name=genre
        )

    for name_actor, surname_actor in actors_list:
        Actor.objects.create(
            first_name=name_actor,
            last_name=surname_actor
        )

    Genre.objects.filter(
        name="Dramma").update(name="Drama"
                              )
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu"
    ).update(
        first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
