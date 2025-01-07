import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Drama")
    Genre.objects.create(name="Comedy")

    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="George", last_name="Clooney")
    Actor.objects.create(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Drama").update(name="Drama Updated")

    Actor.objects.filter(first_name="Jaden", last_name="Smith").update(
        first_name="Jaden Updated", last_name="Smith Updated"
    )

    Genre.objects.filter(name="Drama Updated").delete()

    Actor.objects.filter(first_name="Jaden Updated").delete()

    return Actor.objects.order_by("last_name")
