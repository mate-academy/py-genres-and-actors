import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor
from db.models import Genre


def main() -> QuerySet:

    genres = ["Western", "Action", "Dramma"]

    for genre in genres:
        Genre.objects.create(name=genre,)

    actors = [
        {"name": "George", "surname": "Klooney"},
        {"name": "Kianu", "surname": "Reaves"},
        {"name": "Scarlett", "surname": "Keegan"},
        {"name": "Will", "surname": "Smith"},
        {"name": "Jaden", "surname": "Smith"},
        {"name": "Scarlett", "surname": "Johansson"}
    ]
    for actor in actors:
        Actor.objects.create(
            first_name=actor["name"],
            last_name=actor["surname"],
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name").all()
