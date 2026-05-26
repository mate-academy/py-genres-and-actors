import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Cslooney"),
        ("Keoanu", "Reeves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    george = Actor.objects.get(first_name="George", last_name="Cslooney")
    george.last_name = "Clooney"
    george.save()

    keanu = Actor.objects.get(first_name="Keoanu", last_name="Reeves")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
