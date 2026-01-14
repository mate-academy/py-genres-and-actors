import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


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

    actor_objects = [Actor(first_name=name, last_name=surname)
                     for name, surname in actors]
    Actor.objects.bulk_create(actor_objects)

    drama = Genre.objects.filter(name="Dramma")
    drama.update(name="Drama")

    clooney = Actor.objects.filter(last_name="Klooney")
    clooney.update(last_name="Clooney")

    clooney = Actor.objects.filter(last_name="Reaves")
    clooney.update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
