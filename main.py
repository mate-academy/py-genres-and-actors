import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre

objects_to_create = {
    "geners": ("Western", "Action", "Dramma"),
    "actors": {
        "actors_names": (
            "George",
            "Kianu",
            "Scarlett",
            "Will",
            "Jaden",
            "Scarlett",
        ),
        "actors_last_names": (
            "Klooney",
            "Reaves",
            "Keegan",
            "Smith",
            "Smith",
            "Johansson",
        ),
    }
}


def main() -> QuerySet:
    for f_name, l_name in zip(
            objects_to_create["actors"]["actors_names"],
            objects_to_create["actors"]["actors_last_names"],
    ):
        Actor.objects.create(first_name=f_name, last_name=l_name)

    for genre_name in objects_to_create["geners"]:
        Genre.objects.create(name=genre_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
