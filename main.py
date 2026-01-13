import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:

    cinema_area = {
        "genre":
            [
                "Western",
                "Action",
                "Dramma"
            ],
        "actor":
            [
                "George Klooney",
                "Kianu Reaves",
                "Scarlett Keegan",
                "Will Smith",
                "Jaden Smith",
                "Scarlett Johansson"
            ]
    }

    for compound in cinema_area:
        if compound == "genre":
            for work_genre in cinema_area[compound]:
                Genre.objects.create(name=work_genre)
        if compound == "actor":
            for work_actor in cinema_area[compound]:
                actor_breakdown = work_actor.split()
                Actor.objects.create(
                    first_name=actor_breakdown[0],
                    last_name=actor_breakdown[1]
                )

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    actor_return = (
        Actor.objects.filter(last_name="Smith").order_by("first_name")
    )

    return actor_return


if __name__ == "__main__":
    main()
