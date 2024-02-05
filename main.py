import init_django_orm  # noqa: F401

from django.db.models import Q
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_items = ["Western", "Action", "Dramma"]
    actor_items = [("George", "Klooney"),
                   ("Kianu", "Reaves"),
                   ("Scarlett", "Keegan"),
                   ("Will", "Smith"),
                   ("Jaden", "Smith"),
                   ("Scarlett", "Johansson")]
    for item in genre_items:
        Genre.objects.create(
            name=item,
        )
    for first_item, second_item in actor_items:
        Actor.objects.create(
            first_name=first_item,
            last_name=second_item,
        )

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    Genre.objects.filter(
        name="Action",
    ).delete()
    Actor.objects.filter(Q(
        first_name="Scarlett"
    ) & Q(
        last_name__isnull=False
    )).delete()

    actors_query = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return actors_query
