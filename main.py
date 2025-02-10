import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor
from db.models import Genre

def main() -> QuerySet:
    create_actor("George", "Klooney")
    create_actor("Kianu", "Reaves")
    create_actor("Scarlett", "Keegan")
    create_actor("Will", "Smith")
    create_actor("Jaden", "Smith")
    create_actor("Scarlett", "Johansson")

    create_genre("Western")
    create_genre("Action")
    create_genre("Dramma")

    Genre.objects.filter(
        name="Dramma"
    ).update(
        name="Drama",
    )

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney",
    ).update(
        last_name="Clooney"
    )

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")

def create_actor(first_name, last_name) -> None:
    Actor.objects.create(
        first_name=first_name,
        last_name=last_name,
    )



def create_genre(name) -> None:
    Genre.objects.create(
        name=name,
    )

