import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor

actors = (
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson"),
)

genres = (
    ("Western",),
    ("Action",),
    ("Dramma",),
)


def main() -> QuerySet:
    for genre, in genres:
        Genre.objects.create(name=genre)

    for fname, lname in actors:
        Actor.objects.create(first_name=fname, last_name=lname)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    genre_action = Genre.objects.get(name="Action")
    genre_action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
