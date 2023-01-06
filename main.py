import init_django_orm  # noqa: F401

from db.models import Actors, Genres


def main() -> any:
    Actors.objects.filter().delete()
    Genres.objects.filter().delete()
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]

    for genre in genres:
        Genres.objects.create(name=genre)

    for actor in actors:
        first_name, last_name = actor.split()
        Actors.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genres.objects.filter(name="Dramma").update(name="Drama")

    Actors.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actors.objects.filter(
        first_name="Kianu"
    ).update(first_name="Keanu", last_name="Reeves")

    Genres.objects.filter(name="Action").delete()

    Actors.objects.filter(first_name="Scarlett").delete()



    return Actors.objects.filter(last_name="Smith").order_by("first_name")

main()
