import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def get_firstname_lastname_from_full_name(fullname: str) -> dict:
    data = fullname.split()
    return {"first_name": data[0], "last_name": data[1]}


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Dramma"]
    for curr_item in genres_to_create:
        Genre.objects.create(
            name=curr_item
        )

    actors_to_create = [
        get_firstname_lastname_from_full_name("George Klooney"),
        get_firstname_lastname_from_full_name("Kianu Reaves"),
        get_firstname_lastname_from_full_name("Scarlett Keegan"),
        get_firstname_lastname_from_full_name("Will Smith"),
        get_firstname_lastname_from_full_name("Jaden Smith"),
        get_firstname_lastname_from_full_name("Scarlett Johansson"),
    ]
    for actor_data in actors_to_create:
        Actor.objects.create(
            **actor_data
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        **get_firstname_lastname_from_full_name("George Klooney")
    ).update(last_name="Clooney")

    Actor.objects.filter(
        **get_firstname_lastname_from_full_name("Kianu Reaves")
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
