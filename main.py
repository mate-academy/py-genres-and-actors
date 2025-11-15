from django.db.models import QuerySet
import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main() -> QuerySet:
    # CREATE
    new_genres = ["Western", "Action", "Dramma"]
    for genre_name in new_genres:
        Genre.objects.create(name=genre_name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Keegan"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # UPDATE
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
