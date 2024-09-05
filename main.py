import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genry_list = ["Western", "Action", "Dramma"]

    for genre in genry_list:
        Genre.objects.create(
            name=genre
        )

    actor_list_full_name = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for first, second in actor_list_full_name:
        Actor.objects.create(
            first_name=first,
            last_name=second,
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
