import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_list = ["Western", "Action", "Dramma"]
    actor_list = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]

    for genre in genre_list:
        Genre.objects.create(
            name=genre
        )

    for actor_data in actor_list:
        Actor.objects.create(**actor_data)

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")


if __name__ == "__main__":
    main()
