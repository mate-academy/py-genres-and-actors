import init_django_orm  # noqa: F401

from db.models import Genre, Actor


genres = [
    "Genre",
    "Action",
    "Dramma"
]

actors = [
    (
        "George",
        "Kianu",
        "Scarlett",
        "Will",
        "Jaden",
        "Scarlett"
    ),

    (
        "Klooney",
        "Reaves",
        "Keegan",
        "Smith",
        "Smith",
        "Johansson"
    )

]


def main() -> None:
    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, second_name in actors:
        Actor.objects.create(
            first_name=first_name[0],
            last_name=second_name[1]
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klonney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    Actor.objects.get(
        last_name="Smith"
    )
