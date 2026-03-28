import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Drama"]
    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Keanu", "last_name": "Reeves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]

    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    for actor_data in actors:
        Actor.objects.create(**actor_data)

    Genre.objects.filter(name="Drama").update(name="Drama")

    Actor.objects.filter(first_name="George",
                         last_name="Klooney"
                         ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reeves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    result = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return result
