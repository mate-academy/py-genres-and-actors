import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Dramma"]
    for genre_name in genres_to_create:
        Genre.objects.create(name=genre_name)

    actors_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genre_to_update = Genre.objects.get(name="Dramma")
    genre_to_update.name = "Drama"
    genre_to_update.save()
    actor = Actor.objects.get(last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()
    actor = Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    smiths = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return smiths
