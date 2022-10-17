import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.bulk_create(
        [
            Genre(name="Western"),
            Genre(name="Action"),
            Genre(name="Dramma")
        ]
    )

    Actor.objects.bulk_create(
        [
            Actor(
                first_name="George",
                last_name="Klooney",
            ),
            Actor(
                first_name="Kianu",
                last_name="Reaves",
            ),
            Actor(
                first_name="Scarlett",
                last_name="Keegan",
            ),
            Actor(
                first_name="Will",
                last_name="Smith",
            ),
            Actor(
                first_name="Jaden",
                last_name="Smith",
            ),
            Actor(
                first_name="Scarlett",
                last_name="Johansson",
            )
        ]
    )
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    old_name = [["George", "Klooney"], ["Kianu", "Reaves"]]
    new_name = [["George", "Clooney"], ["Keanu", "Reeves"]]
    for old, new in zip(old_name, new_name):
        old_first_name, old_last_name = old
        new_first_name, new_last_name = new
        Actor.objects.filter(
            first_name=old_first_name,
            last_name=old_last_name,
        ).update(
            first_name=new_first_name,
            last_name=new_last_name,)

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
