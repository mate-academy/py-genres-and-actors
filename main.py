
from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]

    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    updates = [
        ("George", "Klooney", "George", "Clooney"),
        ("Kianu", "Reaves", "Keanu", "Reeves"),
    ]

    for old_first, old_last, new_first, new_last in updates:
        Actor.objects.filter(
            first_name=old_first,
            last_name=old_last
        ).update(
            first_name=new_first,
            last_name=new_last
        )

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
