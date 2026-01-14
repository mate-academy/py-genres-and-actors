import init_django_orm  # noqa: F401
from db.models import Genre, Actor

from django.db.models import QuerySet


genres = [
    "Western", "Action", "Dramma"
]

actors = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def main() -> QuerySet:
    for genre in genres:
        Genre.objects.create(name=genre)
    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
