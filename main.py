import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    film_genres = ["Western", "Action", "Dramma"]
    actors = [
        ["George", "Klooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"]
    ]

    for genre in film_genres:       # creating Genre table (CREATE)
        Genre.objects.create(name=genre)

    for actor in actors:        # creating Actor table (CREATE)
        Actor.objects.create(
            first_name=actor[0],
            last_name=actor[1]
        )

    # read from Actors table (READ)
    read_from_table = Actor.objects.filter(last_name="Smith").order_by("first_name")

    # updating Genre table (UPDATE)
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # updating Actor table (UPDATE)
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    # updating Actor table (UPDATE)
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").\
        update(first_name="Keanu", last_name="Reeves")

    # deleting from Genre table (DELETE)
    Genre.objects.filter(name="Action").delete()

    # deleting from Actor table (DELETE)
    Actor.objects.filter(first_name="Scarlett").delete()

    return read_from_table


if __name__ == "main":
    main()
