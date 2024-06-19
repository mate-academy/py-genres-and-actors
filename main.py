import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # create
    genres_names_to_create = ["Western", "Action", "Dramma"]
    for genre_name in genres_names_to_create:
        Genre.objects.create(
            name=genre_name
        )

    actors_names_to_create = [
        "George Klooney", "Kianu Reaves", "Scarlett Keegan",
        "Will Smith", "Jaden Smith", "Scarlett Johansson"
    ]
    for actor_name in actors_names_to_create:
        actor_name_dict = {"first_name": actor_name.split()[0],
                           "last_name": actor_name.split()[1]}
        Actor.objects.create(**actor_name_dict)

    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # a - automatization
    actors_to_update = {
        "names_to_update": [
            "George Klooney", "Kianu Reaves"
        ],
        "new_atrbs": [
            {
                "last_name": "Clooney",
            },
            {
                "first_name": "Keanu", "last_name": "Reeves"
            }
        ]
    }
    for index in range(len(actors_to_update["names_to_update"])):
        actor_name_dict = {
            "first_name":
                actors_to_update["names_to_update"][index].split()[0],
            "last_name":
                actors_to_update["names_to_update"][index].split()[1]
        }
        Actor.objects.filter(
            **actor_name_dict
        ).update(
            **actors_to_update["new_atrbs"][index]
        )

    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
