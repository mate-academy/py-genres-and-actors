import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    for genre in ("Western", "Action", "Dramma"):
        Genre.objects.create(
            name=genre,
        )

    actors_to_add = [("George", "Klooney"),
                     ("Kianu", "Reaves"),
                     ("Scarlett", "Keegan"),
                     ("Will", "Smith"),
                     ("Jaden", "Smith"),
                     ("Scarlett", "Johansson")]

    for first_name_, last_name_ in actors_to_add:
        Actor.objects.create(
            first_name=first_name_,
            last_name=last_name_
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")

    updates = [
        ("George", "Klooney", "George", "Clooney"),
        ("Kianu", "Reaves", "Keanu", "Reeves")
    ]

    for (first_name, last_name,
         new_first_name, new_last_name) in updates:
        Actor.objects.filter(
            first_name=first_name,
            last_name=last_name
        ).update(
            first_name=new_first_name,
            last_name=new_last_name
        )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
