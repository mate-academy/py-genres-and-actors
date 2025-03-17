import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]

    for genre in genres:
        Genre.objects.create(
            name=genre
        )

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for fname_item, lname_item in actors:
        Actor.objects.create(
            first_name=fname_item,
            last_name=lname_item
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(
        name="Drama"
    )

    Actor.objects.filter(
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

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    Genre.objects.filter(
        name="Action"
    ).delete()

    return Actor.objects.all().filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    )
