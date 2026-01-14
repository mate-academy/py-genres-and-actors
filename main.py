import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    film_genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    # creating records in Genre table (CREATE)
    for genre in film_genres:
        Genre.objects.create(name=genre)

    # creating records in Actor table (CREATE)
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # read from Actors table (READ)
    actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    # updating records in Genre table (UPDATE)
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # updating records in Actor table (UPDATE)
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    # updating records in Actor table (UPDATE)
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # deleting records from Genre table  (DELETE)
    Genre.objects.filter(name="Action").delete()

    # deleting records from Actor table  (DELETE)
    Actor.objects.filter(first_name="Scarlett").delete()

    return actors
