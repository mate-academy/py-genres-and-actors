import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre

genres = ("Western", "Action", "Dramma")
actors = (
    "George Klooney",
    "Kianu Reaves",
    "Scarlett Keegan",
    "Will Smith",
    "Jaden Smith",
    "Scarlett Johansson",
)


def main() -> QuerySet:
    # create
    [
        Actor.objects.create(
            first_name=actor.split()[0], last_name=actor.split()[1]
        )
        for actor in actors
    ]
    [Genre.objects.create(name=genre) for genre in genres]
    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
    # <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

    # Можливо потрібно переопреділити магічний метод __repr__ але то не точно)

    print(Genre.objects.all())
    # <QuerySet [<Genre: Western>, <Genre: Drama>]>

    print(Actor.objects.all())
    # <QuerySet [<Actor: George Clooney>,
    # <Actor: Keanu Reeves>, <Actor: Will Smith>, <Actor: Jaden Smith>]>
