import init_django_orm  # noqa: F401

from django.db.models import QuerySet  # noqa: F401

from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    genres = ("Western", "Dramma", "Action")
    Genre.objects.bulk_create([Genre(genre_name=genre) for genre in genres])

    actors = (
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    )

    Actor.objects.bulk_create([
        Actor(
            first_name=first_name,
            last_name=last_name
        ) for first_name, last_name in actors])

    Genre.objects.filter(genre_name="Dramma").update(genre_name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(genre_name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
