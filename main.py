import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    genres = (["Western", "Action", "Dramma"])
    names = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for genre in genres:
        Genre.objects.create(name=genre)

    for first, last in names:
        Actor.objects.create(first_name=first, last_name=last)

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()
    george = Actor.objects.get(first_name="George", last_name="Klooney")
    george.first_name = "George"
    george.last_name = "Clooney"
    george.save()
    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
