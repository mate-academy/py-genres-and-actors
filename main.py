import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


genre_items = (
    "Western",
    "Action",
    "Dramma"
)
actor_items = (
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
)


def main() -> QuerySet:
    for genre in genre_items:
        Genre.objects.create(
            name=genre
        )
    for item_first, item_second in actor_items:
        Actor.objects.create(
            first_name=item_first,
            last_name=item_second
        )
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
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
        last_name="Smith"
    ).order_by("first_name")
