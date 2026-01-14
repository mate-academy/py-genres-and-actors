import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for genre in genres:
        Genre.objects.create(name=genre)
    for name, surname in actors:
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )
    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()
    clooney = Actor.objects.get(last_name="Klooney")
    clooney.last_name = "Clooney"
    clooney.save()
    reeves = Actor.objects.get(last_name="Reaves")
    reeves.first_name = "Keanu"
    reeves.last_name = "Reeves"
    reeves.save()
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
