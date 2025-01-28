from django.db.models import QuerySet
import init_django_orm  # noqa: F401
from db.models import Actor, Genre


def main() -> QuerySet:
    genre_to_create = ["Western",
                       "Action",
                       "Dramma"]

    actor_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    # Create
    for data in genre_to_create:
        Genre.objects.create(name=data, )

    for data_name, data_last_name in actor_to_create:
        Actor.objects.create(
            first_name=data_name,
            last_name=data_last_name
        )

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
