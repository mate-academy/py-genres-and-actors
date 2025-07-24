import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


genres = ["Action", "Western", "Dramma"]
actors = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def main() -> QuerySet:
    for genre in genres:
        Genre.objects.create(
            name=genre
        )

    for actor_name, actor_surname in actors:
        Actor.objects.create(
            first_name=actor_name,
            last_name=actor_surname
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    qr_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return qr_actors
