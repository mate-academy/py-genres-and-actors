import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson"
    )

if __name__ == "__main__":
    main()