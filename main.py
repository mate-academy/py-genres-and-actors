import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    # CREATE
    for genre in genres:
        Genre.objects.create(
            name=genre
        )
    for item_first, item_second in actors:
        Actor.objects.create(
            first_name=item_first,
            last_name=item_second
        )

    # UPDATE
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    actor = Actor.objects.filter(first_name="Kianu")
    actor.update(first_name="Keanu", last_name="Reeves")

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors.all()
