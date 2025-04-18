import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    name_genres = "Western", "Action", "Dramma"
    name_actor = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for item  in name_genres:
        Genre.objects.create(name=item)

    for item_first, item_last in name_actor:
        Actor.objects.create(
            first_name=item_first,
            last_name=item_last
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu",
             last_name="Reeves")
    Genre.objects.filter(name="Action"
                         ).delete()
    Actor.objects.filter(
        first_name="Scarlett").delete()
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
