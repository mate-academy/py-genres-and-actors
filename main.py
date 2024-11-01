from setuptools.extern import names

import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:

    # genres = ["Western", "Action", "Dramma"]
    #
    # actors = [
    #     ("George", "Klooney"),
    #     ("Kianu", "Reaves"),
    #     ("Scarlett", "Keegan"),
    #     ("Will", "Smith"),
    #     ("Jaden", "Smith"),
    #     ("Scarlett", "Johansson"),
    # ]

    create_data = {
        "genres": ["Western", "Action", "Dramma"],
        "actors": [
            ("George", "Klooney"),
            ("Kianu", "Reaves"),
            ("Scarlett", "Keegan"),
            ("Will", "Smith"),
            ("Jaden", "Smith"),
            ("Scarlett", "Johansson"),
        ]
    }


    for genre in create_data.get("genres"):
        Genre.objects.create(name=genre)

    for first_name, last_mane in create_data.get("actors"):
        Actor.objects.create(first_name=first_name, last_name=last_mane)


    get_genre = Genre.objects.get(name="Dramma")
    # print(get_genre.name)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    get_genre = Genre.objects.get(name="Drama")
    # print(get_genre.name)

    get_actor = Actor.objects.get(first_name="George")
    # print(get_actor.first_name, get_actor.last_name)

    Actor.objects.filter(first_name="George").update(last_name="Clooney")

    get_actor = Actor.objects.get(first_name="George")
    # print(get_actor.first_name, get_actor.last_name)

    get_actor = Actor.objects.get(first_name="Kianu")
    # print(get_actor.first_name, get_actor.last_name)

    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu", last_name="Reeves")

    get_actor = Actor.objects.get(first_name="Keanu")
    # print(get_actor.first_name, get_actor.last_name)


    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


# if __name__ == "__main__":
#     print(main())
