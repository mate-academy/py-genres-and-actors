import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


genres = [
    {"name": "Western"},
    {"name": "Action"},
    {"name": "Dramma"}
]

actors = [
    {"first_name": "George", "last_name": "Klooney"},
    {"first_name": "Kianu", "last_name": "Reaves"},
    {"first_name": "Scarlett", "last_name": "Keegan"},
    {"first_name": "Will", "last_name": "Smith"},
    {"first_name": "Jaden", "last_name": "Smith"},
    {"first_name": "Scarlett", "last_name": "Johansson"}
]


def main() -> QuerySet:
    for genre in genres:
        Genre.objects.create(
            name=genre["name"]
        )

    for actor in actors:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    jorge = Actor.objects.get(first_name="George")
    jorge.last_name = "Clooney"
    jorge.save()

    keanu = Actor.objects.get(first_name="Kianu")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    action = Genre.objects.get(name="Action")
    action.delete()

    actresses = Actor.objects.filter(first_name="Scarlett")
    actresses.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
