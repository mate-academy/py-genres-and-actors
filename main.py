import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    genres_list = [("Western"), ("Action"), ("Dramma")]
    actors_list = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for genre in genres_list:
        Genre.objects.create(name=genre)

    for name, surname in actors_list:
        Actor.objects.create(first_name=name, last_name=surname)

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    actor = Actor.objects.get(first_name="George")
    actor.last_name = "Clooney"
    actor.save()

    actor = Actor.objects.get(last_name="Reaves")
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    Genre.objects.get(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
