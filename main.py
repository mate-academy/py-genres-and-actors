from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]
    for firstname, lastname in actors:
        Actor.objects.create(
            first_name=firstname,
            last_name=lastname
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
