import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet | None:
    put_values("Genre", [("Western",), ("Action",), ("Dramma",)])
    put_values(
        "Actor",
        [
            ("George", "Klooney"),
            ("Kianu", "Reaves"),
            ("Scarlett", "Keegan"),
            ("Will", "Smith"),
            ("Jaden", "Smith"),
            ("Scarlett", "Johansson"),
        ],
    )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def put_values(table_name: str, data: list) -> None:
    """
    Will create a several table raws in one call
    """
    if table_name == "Genre":
        for values in data:
            if len(values) != 1:
                raise ValueError("Genre must have one field name")
            Genre.objects.create(name=values[0])
    if table_name == "Actor":
        for values in data:
            if len(values) != 2:
                raise ValueError("Actor must have two fields name and surname")
            Actor.objects.create(first_name=values[0], last_name=values[1])
