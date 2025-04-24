import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres_list = ["Western", "Action", "Dramma"]
    for genre in genres_list:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Scarlett", "Johansson"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(first_name="George")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu")
     .update(first_name="Keanu", last_name="Reaves"))

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
