import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.bulk_create(
        [
            Genre(name="Western"),
            Genre(name="Action"),
            Genre(name="Dramma")
        ]
    )

    Actor.objects.bulk_create(
        [
            Actor(first_name="George", last_name="Klooney"),
            Actor(first_name="Kianu", last_name="Reaves"),
            Actor(first_name="Will", last_name="Smith"),
            Actor(first_name="Jaden", last_name="Smith"),
            Actor(first_name="Scarlett", last_name="Johansson"),
        ]
    )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    george = Actor.objects.get(first_name="George", last_name="Klooney")
    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")

    george.last_name = "Clooney"
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"

    Actor.objects.bulk_update([george, kianu], ["first_name", "last_name"])

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = (Actor.objects.filter(last_name="Smith")
                    .order_by("first_name"))
    return smith_actors
