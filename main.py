import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.get(name="Western")
    Genre.objects.get(name="Action")
    Genre.objects.get(name="Dramma")
    Actor.objects.get(first_name="George", last_name="Klooney")
    Actor.objects.get(first_name="Kianu", last_name="Reaves")
    Actor.objects.get(first_name="Scarlett", last_name="Keegan")
    Actor.objects.get(first_name="Will", last_name="Smith")
    Actor.objects.get(first_name="Jaden", last_name="Smith")
    Actor.objects.get(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(fist_name="George",
                         last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu",
                         last_name="Reaves").update(last_name="Reeves")

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
