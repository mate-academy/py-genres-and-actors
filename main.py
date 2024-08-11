import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    genres = ["Western", "Action", "Dramma"]

    for first_name_, last_name_ in actors:
        Actor.objects.create(
            first_name=first_name_,
            last_name=last_name_
        )

    for genre in genres:
        Genre.objects.create(
            name=genre,
        )

    # Update
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    # Delete
    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    # Return
    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
