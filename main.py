import init_django_orm  # noqa: F401
from db.models import Actor, Genre

from django.db.models import QuerySet


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]

    genres_objects = [Genre(name=genre) for genre in genres]
    Genre.objects.bulk_create(genres_objects)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    actors_objects = [
        Actor(first_name=first, last_name=second)
        for first, second in actors
    ]
    Actor.objects.bulk_create(actors_objects)

    drama = Genre.objects.filter(name="Dramma")
    drama.update(name="Drama")

    clooney = Actor.objects.filter(last_name="Klooney")
    clooney.update(last_name="Clooney")

    reeves = Actor.objects.filter(last_name="Reaves")
    reeves.update(
        first_name="Keanu",
        last_name="Reeves"
    )

    action = Genre.objects.filter(name="Action")
    action.delete()

    scarlets = Actor.objects.filter(first_name="Scarlett")
    scarlets.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
