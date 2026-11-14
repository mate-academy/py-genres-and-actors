import init_django_orm  # noqa: F401
from db.models import Actor, Genre

from django.db.models import QuerySet


def main() -> QuerySet:
    genre_list = ["Western", "Action", "Dramma"]
    actor_list = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]

    for genre in genre_list:
        Genre.objects.create(name=genre)

    for actor in actor_list:
        splitted_actor = actor.split()
        Actor.objects.create(
            first_name=splitted_actor[0], last_name=splitted_actor[1]
        )
