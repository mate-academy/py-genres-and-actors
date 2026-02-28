import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # populate tables with data
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=f"{genre}")

    actors = [
        ("George", "Klooney"), ("Kianu", "Reaves"), ("Scarlett", "Keegan"),
        ("Will", "Smith"), ("Jaden", "Smith"), ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=f"{first_name}",
            last_name=f"{last_name}"
        )

    # update data
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # delete data
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # return QuerySet
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
