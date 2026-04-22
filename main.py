import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for (name,) in genres:
        Genre.objects.create(name=name)

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    for genre in Genre.objects.filter(name="Dramma"):
        genre.name = "Drama"
        genre.save()

    for actor in Actor.objects.filter(first_name="George"):
        actor.last_name = "Clooney"
        actor.save()

    for actor in Actor.objects.filter(first_name="Kianu"):
        actor.first_name = "Keanu"
        actor.last_name = "Reeves"
        actor.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
