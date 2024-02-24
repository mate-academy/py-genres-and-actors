import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    # CREATE
    genres_to_create = ["Western", "Action", "Dramma"]
    for element in genres_to_create:
        Genre.objects.create(name=element)

    actors_to_create = {"first_name": ["George", "Kianu", "Scarlett",
                                       "Will", "Jaden", "Scarlett"],
                        "last_name": ["Klooney", "Reaves", "Keegan",
                                      "Smith", "Smith", "Johansson"]}
    for first_name, last_name in zip(actors_to_create["first_name"],
                                     actors_to_create["last_name"]):
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # UPDATE
    Genre.objects.filter(name="Dramma", ).update(name="Drama")
    (Actor.objects.filter(first_name="George", last_name="Klooney", )
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves", ).
     update(first_name="Keanu", last_name="Reeves"))

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    # READ
    expected_result = (Actor.objects.filter(last_name="Smith")
                       .order_by("first_name"))
    return expected_result


if __name__ == "__main__":
    main()
