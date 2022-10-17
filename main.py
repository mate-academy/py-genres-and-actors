import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    for genre in ["Western", "Action", "Dramma"]:
        Genre.objects.create(
            name=genre,
        )

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        first_name="George",
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
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return smith_actors
