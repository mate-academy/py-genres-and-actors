import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    actors = Actor.objects.filter(
        last_name="Smith",
    ).order_by(
        "first_name",)

    return actors

    genres = Genre.objects.all()
    return genres

print(main())
# <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

print(Genre.objects.all())
# <QuerySet [<Genre: Western>, <Genre: Drama>]>

print(Actor.objects.all())
# <QuerySet [<Actor: George Clooney>, <Actor: Keanu Reeves>, <Actor: Will Smith>, <Actor: Jaden Smith>]>

if __name__ == "__main__":
    main()