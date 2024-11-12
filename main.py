import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    Actor.objects.all().delete()
    Genre.objects.all().delete()

    actors_data = [
        {"first_name": "George", "last_name": "Clooney"},
        {"first_name": "Keanu", "last_name": "Reeves"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
    ]

    for actor in actors_data:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    genres_data = [
        {"name": "Western"},
        {"name": "Drama"},
    ]

    for genre in genres_data:
        Genre.objects.create(name=genre["name"])

    actors = Actor.objects.all()

    main_actors = actors.filter(last_name="Smith").order_by("first_name")

    return main_actors
