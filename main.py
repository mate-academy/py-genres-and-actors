import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_names = ["Western", "Action", "Drama"]
    for name in genre_names:
        Genre.objects.get_or_create(name=name)

    actor_details = [
        {"first_name": "George", "last_name": "Clooney"},
        {"first_name": "Keanu", "last_name": "Reeves"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]
    for actor in actor_details:
        Actor.objects.get_or_create(**actor)

    Actor.objects.filter(first_name="Scarlett").delete()
    Genre.objects.filter(name="Action").delete()

    smith_actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smith_actors
