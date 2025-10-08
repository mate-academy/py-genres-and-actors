import init_django_orm  # noqa: F401

from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main() -> QuerySet:
    for placeholder in ["Western", "Action", "Dramma"]:
        Genre.objects.create(
            name=placeholder,
        )
    for fname, lname in [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),]:
            Actor.objects.create(
            first_name = fname,
            last_name = lname,
    )
    Genre.objects.filter(
        name = "Dramma"
    ).update(
        name = "Drama"
    )
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    actors_smiths = Actor.objects.filter(last_name="Smith").all().order_by("first_name")

    return actors_smiths

if __name__ == "__main__":
    main()
