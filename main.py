import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    list_of_genres = ["Western", "Action", "Dramma"]
    list_of_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    actors_to_update = [
        ("George", "Klooney", "George", "Clooney"),
        ("Kianu", "Reaves", "Keanu", "Reeves")
    ]
    for genre in list_of_genres:
        Genre.objects.create(
            name=genre
        )
    for name, surname in list_of_actors:
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    for name, surname, new_name, new_surname in actors_to_update:
        Actor.objects.filter(
            first_name=name,
            last_name=surname
        ).update(
            first_name=new_name,
            last_name=new_surname
        )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
