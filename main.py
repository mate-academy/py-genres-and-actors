import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        "George Klooney", "Kianu Reaves", "Scarlett Keegan",
        "Will Smith", "Jaden Smith", "Scarlett Johansson"
    ]

    for genre in genres:
        print(Genre.objects.create(name=genre,))

    for actor in actors:
        first_name, last_name = actor.split()
        print(Actor.objects.create(first_name=first_name, last_name=last_name))

    print(Genre.objects.filter(name="Dramma",).update(name="Drama"))

    print(Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney"))

    print(Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves"))

    Genre.objects.filter(name="Action",).delete()
    Actor.objects.filter(first_name="Scarlett",).delete()

    return Actor.objects.filter(last_name="Smith",).order_by("first_name")


if __name__ == "__main__":
    main()
