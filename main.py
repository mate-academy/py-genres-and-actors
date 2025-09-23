import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    iter_genre = ["Western", "Action", "Dramma"]
    iter_actor = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for _iter in iter_genre:
        Genre.objects.create(
            name=_iter,
        )

    for first_name, last_name in iter_actor:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    # Update
    Genre.objects.filter(
        name="Dramma",
    ).update(
        name="Drama",
    )

    Actor.objects.filter(
        last_name="Klooney",
    ).update(
        last_name="Clooney",
    )

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # Delete
    Genre.objects.filter(
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    # Returned retrieve
    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
