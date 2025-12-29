# main.py
from django.db import connection
from django.db.models import QuerySet

from db.models import Actor, Genre


def _ensure_tables() -> None:
    genre_table = Genre._meta.db_table
    actor_table = Actor._meta.db_table
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS "{genre_table}" (
                "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                "name" varchar(255) NOT NULL
            )
            """
        )
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS "{actor_table}" (
                "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                "first_name" varchar(255) NOT NULL,
                "last_name" varchar(255) NOT NULL
            )
            """
        )


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
