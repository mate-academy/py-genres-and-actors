import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres_data = [
        ("Western",), ("Action",), ("Dramma",)
    ]

    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for name, in genres_data:
        Genre.objects.create(name=name)

    for first, last in actors_data:
        Actor.objects.create(first_name=first, last_name=last)

    genre_1 = Genre.objects.get(name="Dramma")
    genre_1.name = "Drama"
    genre_1.save()

    actor_1 = Actor.objects.get(first_name="George", last_name="Klooney")
    actor_1.last_name = "Clooney"
    actor_1.save()

    actor_2 = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_2.first_name = "Keanu"
    actor_2.last_name = "Reeves"
    actor_2.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    result = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return result
