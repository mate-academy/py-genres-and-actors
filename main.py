import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genre_names = ["Western",
                   "Action",
                   "Dramma"]

    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for name in genre_names:
        Genre.objects.create(name=name)

    for first_name, last_name in actors_data:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        first_name="Kianu"
    ).update(
        first_name="Keanu",
        last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
