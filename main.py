import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:

    Genre.objects.create(
        name="Western"
    )
    action = Genre.objects.create(
        name="Action"
    )
    dramma = Genre.objects.create(
        name="Dramma"
    )

    Actor.objects.create(
        first_name="George", last_name="Klooney"
    )
    Actor.objects.create(
        first_name="Kianu", last_name="Reaves"
    )
    Actor.objects.create(
        first_name="Scarlett", last_name="Keegan"
    )
    Actor.objects.create(
        first_name="Will", last_name="Smith"
    )
    Actor.objects.create(
        first_name="Jaden", last_name="Smith"
    )
    Actor.objects.create(
        first_name="Scarlett", last_name="Johansson"
    )

    dramma.name = "Drama"
    dramma.save()

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney").update(last_name="Clooney")

    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    action.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    last_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return last_smith
