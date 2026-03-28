import init_django_orm  # noqa: F401

from db.models import Genre, Actor

from django.db.models import QuerySet


def main() -> QuerySet:
    genre_names = ["Western", "Action", "Drama"]
    for name in genre_names:
        Genre.objects.get_or_create(name=name)

    actor_info = [
        {"first_name": "George", "last_name": "Clooney"},
        {"first_name": "Keanu", "last_name": "Reeves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]

    for actor in actor_info:
        Actor.objects.get_or_create(**actor)

    if Genre.objects.filter(name="Dramma").exists():
        drama_genre = Genre.objects.get(name="Dramma")
        drama_genre.name = "Drama"
        drama_genre.save()

    if Actor.objects.filter(last_name="Klooney").exists():
        george = Actor.objects.get(last_name="Klooney")
        george.last_name = "Clooney"
        george.save()

    if Actor.objects.filter(first_name="Kianu").exists():
        keanu = Actor.objects.get(first_name="Kianu")
        keanu.first_name = "Keanu"
        keanu.last_name = "Reeves"
        keanu.save()

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
