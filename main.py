# main.py
from django.db import connection
from django.db.models import QuerySet

from db.models import Actor, Genre


def _ensure_tables() -> None:
    existing = set(connection.introspection.table_names())
    with connection.schema_editor() as schema_editor:
        if Genre._meta.db_table not in existing:
            schema_editor.create_model(Genre)
        if Actor._meta.db_table not in existing:
            schema_editor.create_model(Actor)


def main() -> QuerySet[Actor]:
    _ensure_tables()

    genres = [("Western",), ("Action",), ("Dramma",)]
    for (name,) in genres:
        Genre.objects.create(name=name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney",
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves",
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
