import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre

GENRES = [
    "Western",
    "Action",
    "Dramma"
]

ACTORS = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def create() -> None:
    for genre_name in GENRES:
        genre = Genre.objects.create(name=genre_name)
        genre.save()
    for first, last in ACTORS:
        actor = Actor.objects.create(first_name=first, last_name=last)
        actor.save()


def update() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )


def delete() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def get_return() -> QuerySet:
    query_set = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return query_set


def main() -> QuerySet:
    create()
    update()
    delete()
    return get_return()
