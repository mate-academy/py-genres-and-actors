import init_django_orm  # noqa: F401

from db.models import Genre, Actor
from django.db.models import QuerySet, Model

genres = [
    {"name": "Western"},
    {"name": "Action"},
    {"name": "Dramma"},
]

actors = [
    {"first_name": "George", "last_name": "Klooney"},
    {"first_name": "Kianu", "last_name": "Reaves"},
    {"first_name": "Scarlett", "last_name": "Keegan"},
    {"first_name": "Will", "last_name": "Smith"},
    {"first_name": "Jaden", "last_name": "Smith"},
    {"first_name": "Scarlett", "last_name": "Johansson"},
]


def create_entries(table_model: type[Model], *args) -> None:
    for arg in args:
        table_model.objects.create(**arg)


create_entries(Genre, *genres)
create_entries(Actor, *actors)

Genre.objects.filter(name="Dramma").update(name="Drama")
Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
Actor.objects.filter(
    first_name="Kianu", last_name="Reaves").update(
    first_name="Keanu", last_name="Reeves"
)

Genre.objects.filter(name="Action").delete()
Actor.objects.filter(first_name="Scarlett").delete()


def main() -> QuerySet:
    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")


print(main())
