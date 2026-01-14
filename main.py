import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        "George Klooney", "Kianu Reaves", "Scarlett Keegan",
        "Will Smith", "Jaden Smith", "Scarlett Johansson"
    ]

    genres_updates = [("Dramma", "Drama")]
    actors_updates = [
        ("George Klooney", "George Clooney"),
        ("Kianu Reaves", "Keanu Reeves")
    ]

    for name in genres:
        Genre.objects.create(
            name=name
        )

    for full_name in actors:
        first_name, last_name = full_name.split()
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    for name_incorrect, name_correct in genres_updates:
        Genre.objects.filter(
            name=name_incorrect
        ).update(name=name_correct)

    for name_incorrect, name_correct in actors_updates:
        Actor.objects.filter(
            first_name=name_incorrect.split()[0],
            last_name=name_incorrect.split()[1]
        ).update(
            first_name=name_correct.split()[0],
            last_name=name_correct.split()[1]
        )

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    actors_filtered = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return actors_filtered


if __name__ == "__main__":
    actors_filtered = main()
    print(actors_filtered)
