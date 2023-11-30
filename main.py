import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = {
        1: {"first_name": "George", "last_name": "Klooney"},
        2: {"first_name": "Kianu", "last_name": "Reaves"},
        3: {"first_name": "Scarlett", "last_name": "Keegan"},
        4: {"first_name": "Will", "last_name": "Smith"},
        5: {"first_name": "Jaden", "last_name": "Smith"},
        6: {"first_name": "Scarlett", "last_name": "Johansson"},
    }

    for genre in genres:
        Genre.objects.create(name=genre)

    for _, actor in actors.items():
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
