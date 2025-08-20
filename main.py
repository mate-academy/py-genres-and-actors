import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")

    Actor.objects.create(
        first_name="George",
        last_name="Clooney",
    )
    Actor.objects.create(
        first_name="Keanu",
        last_name="Reeves",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )

    genre = Genre.objects.get(name="Drama")
    genre.name = "Drama"
    genre.save()

    actor = Actor.objects.get(first_name="George", last_name="Clooney")
    actor.name = "George"
    actor.save()

    actor = Actor.objects.get(first_name="Keanu", last_name="Reeves")
    actor.name = "Keanu"
    actor.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    actors_smith = (
        Actor.objects
        .filter(last_name="Smith")
        .order_by("first_name")
    )
    return actors_smith
