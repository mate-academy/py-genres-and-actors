import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:

    # Create
    genres = ["Western", "Action", "Dramma"]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    names = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for name, surname in names:
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )

    # Update
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu"
    ).update(first_name="Keanu",
             last_name="Reeves")

    # Delete
    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    # Return
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name").all()
