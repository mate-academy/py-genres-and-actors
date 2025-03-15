import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Action")
    print(Genre.objects.all())
    print(Actor.objects.all())


if __name__ == "__main__":
    main()