import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    for name in ("Western", "Action", "Dramma"):
        Genre.objects.create(
            name=name,
        )

    first_names = ("George", "Kianu", "Scarlett",
                   "Will", "Jaden", "Scarlett")
    last_names = ("Klooney", "Reaves", "Keegan",
                  "Smith", "Smith", "Johansson")

    actor_data = [
        Actor(first_name=first, last_name=last) for first, last
        in zip(first_names, last_names)
    ]

    Actor.objects.bulk_create(actor_data)

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="Kianu",
    ).update(first_name="Keanu"), Actor.objects.filter(
        last_name="Reaves",
    ).update(last_name="Reeves"), Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")

    Genre.objects.filter(
        name="Action",
    ).delete(), Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
