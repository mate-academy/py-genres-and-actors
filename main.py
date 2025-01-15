import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor
from db.models import Genre


def main() -> QuerySet:
    genres = ("Western", "Action", "Dramma")
    actors = (
        {"row_first_name" : "George", "row_last_name" : "Klooney"},
        {"row_first_name" : "Kianu", "row_last_name" : "Reaves"},
        {"row_first_name" : "Scarlett", "row_last_name" : "Keegan"},
        {"row_first_name" : "Will", "row_last_name" : "Smith"},
        {"row_first_name" : "Jaden", "row_last_name" : "Smith"},
        {"row_first_name" : "Scarlett", "row_last_name" : "Johansson"},
    )
    for genre in genres:
        Genre.objects.create(
            name=genre
        )
    for actor in actors:
        Actor.objects.create(
            first_name=actor["row_first_name"],
            last_name=actor["row_last_name"]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
