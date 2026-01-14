
from django.db.models import QuerySet
from db.models import Actor
from db.models import Genre


def main() -> QuerySet:

    genre_to_add = ["Western", "Action", "Dramma"]
    actors_to_add = [
        (
            "George",
            "Klooney"
        ),
        (
            "Kianu",
            "Reaves"
        ),
        (
            "Scarlett",
            "Keegan"
        ),
        (
            "Will",
            "Smith"
        ),
        (
            "Jaden",
            "Smith"
        ),
        (
            "Scarlett",
            "Johansson"
        )

    ]
    for genre in genre_to_add:
        Genre.objects.create(name=genre)

    for first, second in actors_to_add:
        Actor.objects.create(
            first_name=first,
            last_name=second)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(
        first_name="George",
        last_name="Klooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))
    genre_to_delete = Genre.objects.filter(name="Action")
    genre_to_delete.delete()
    all_actresses_scarlet = Actor.objects.filter(first_name="Scarlett")
    all_actresses_scarlet.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
