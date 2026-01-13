import init_django_orm  # noqa F401

from django.db.models import QuerySet


from db.models import Genre, Actor


def main() -> QuerySet:
    genres_data = [("Western",), ("Action",), ("Drama",)]

    for genre_name, in genres_data:
        Genre.objects.create(name=genre_name)

    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for first_name, last_name in actors_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Drama").update(name="Drama")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name__startswith="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
