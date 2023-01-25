import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.bulk_create(
        Genre(name=genre)
        for genre in ["Western", "Action", "Dramma"]
    )

    Actor.objects.bulk_create(
        Actor(first_name=name, last_name=name_last)
        for name, name_last in [
            ("George", "Klooney"), ("Kianu", "Reaves"),
            ("Scarlett", "Keegan"), ("Will", "Smith"),
            ("Jaden", "Smith"), ("Scarlett", "Johansson")]
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
