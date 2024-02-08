import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres_to_add = [
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma")
    ]

    Genre.objects.bulk_create(genres_to_add)

    actors_to_add = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for actor in actors_to_add:
        first_name, last_name = actor
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Actor.objects.filter(first_name="Scarlett").delete()
    Genre.objects.filter(name="Action").delete()

    return (Actor.objects.filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    ).values_list(
        "first_name",
        "last_name")
    )
