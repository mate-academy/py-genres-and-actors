import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres_to_add = ["Western", "Action", "Dramma"]
    actors_to_add = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for genres in genres_to_add:
        Genre.objects.create(name=genres)

    for first_name, last_name in actors_to_add:
        Actor.objects.create(
            first_name = first_name,
            last_name = last_name
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    actors_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name").values()

    return actors_smith


if __name__ == "__main__":
    main()
