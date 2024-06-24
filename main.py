import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:

    dataset_genre = ["Western", "Action", "Dramma"]
    for genre in dataset_genre:
        Genre.objects.create(name=genre)

    dataset_actor = [
        ["George", "Clooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"]
    ]

    for actor in dataset_actor:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves").
     update(first_name="Keanu", last_name="Reeves"))

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    actors_with_smith_last_name = (
        Actor.objects.filter(last_name="Smith").order_by("first_name"))

    return actors_with_smith_last_name
