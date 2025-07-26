import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.all().bulk_create([
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma")
    ])

    Actor.objects.all().bulk_create([
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson")
    ])

    Genre.objects.all().filter(name="Dramma").update(name="Drama")

    Actor.objects.all().filter(last_name="Klooney").update(last_name="Clooney")

    Actor.objects.all().filter(first_name="Kianu").update(first_name="Keanu")

    Actor.objects.all().filter(last_name="Reaves").update(last_name="Reeves")

    Genre.objects.all().filter(name="Action").delete()

    Actor.objects.all().filter(first_name="Scarlett").delete()

    return  Actor.objects.all().filter(last_name="Smith").order_by("first_name")




