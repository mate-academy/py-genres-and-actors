import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(genre)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Smith", "Wilson"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name, last_name)

    Genre.objects.filter(
        name='Dramma'
    ).update("Drama")

    Actor.objects.filter(
        last_name='Klooney'
    ).update("Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name='Reaves'
    ).update("Keanu", "Reeves")

    Genre.objects.filter(
        name='Action'
    ).delete()

    Genre.objects.filter(
        name='Scarlett'
    ).delete()

    return QuerySet(
        Actor.objects.filter(
            last_name='Smith'
        ).order_by('first_name')
    )


if __name__ == '__main__':
    print(main())
    # <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

    print(Genre.objects.all())
    # <QuerySet [<Genre: Western>, <Genre: Drama>]>

    print(Actor.objects.all())
