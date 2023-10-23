import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:

    Actor.objects.all().delete()
    Genre.objects.all().delete()
    Genre.objects.create(name="Western",)
    Genre.objects.create(name="Action",)
    Genre.objects.create(name="Dramma",)

    actors_first_name = ["George", "Kianu", "Scarlett",
                         "Will", "Jaden", "Scarlett"]
    actors_last_name = ["Klooney", "Reaves", "Keegan",
                        "Smith", "Smith", "Johansson"]

    for number in range(len(actors_first_name)):
        Actor.objects.create(
            first_name=actors_first_name[number],
            last_name=actors_last_name[number]
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    result = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return result


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())
