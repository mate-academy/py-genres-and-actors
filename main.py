import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres: QuerySet[Genre] = Genre.objects
    actors: QuerySet[Actor] = Actor.objects

    genres_list = ["Western", "Action", "Dramma"]

    genres.bulk_create([Genre(name=name) for name in genres_list])

    actors_list = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    actors.bulk_create(
        [
            Actor(first_name=first, last_name=last)
            for first, last in actors_list
        ]
    )

    genres.filter(name="Dramma").update(name="Drama")
    actors.filter(last_name="Klooney").update(last_name="Clooney")
    actors.filter(last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    genres.filter(name="Action").delete()
    actors.filter(first_name="Scarlett").delete()

    return actors.filter(last_name="Smith").order_by("first_name")
