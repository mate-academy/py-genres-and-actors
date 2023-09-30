import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_list = ["Western", "Action", "Dramma"]
    for data_genre in genre_list:
        Genre.objects.create(
            name=data_genre,
        )
    actor_list = [
        ["George", "Klooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"]
    ]
    for data_actor in actor_list:
        Actor.objects.create(
            first_name=data_actor[0],
            last_name=data_actor[1],
        )
    Genre.objects.filter(
        name="Action",
    ).delete()
    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney",)
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(
        first_name="Keanu",
        last_name="Reeves",
    )
    Genre.objects.filter(
        name="Action",
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()
    results = Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
    print(results)
    return results


if __name__ == "__main__":
    main()
