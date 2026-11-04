import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    genre_dramma = Genre.objects.get(name="Dramma")
    genre_dramma.name = "Drama"
    genre_dramma.save()

    actor_george = Actor.objects.get(first_name="George", last_name="Klooney")
    actor_george.last_name = "Clooney"
    actor_george.save()

    actor_kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_kianu.first_name = "Keanu"
    actor_kianu.last_name = "Reeves"
    actor_kianu.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
