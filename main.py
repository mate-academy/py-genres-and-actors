import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:

    # Actor.objects.all().delete()
    # Genre.objects.all().delete()
    list_of_genre = ["Western", "Action", "Dramma"]
    for genre in list_of_genre:
        Genre.objects.create(name=genre,)

    actors_list = [("George", "Klooney"),
                   ("Kianu", "Reaves"),
                   ("Scarlett", "Keegan"),
                   ("Will", "Smith"),
                   ("Jaden", "Smith"),
                   ("Scarlett", "Johansson")]

    for first_name, last_name in actors_list:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    result = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return result


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())
