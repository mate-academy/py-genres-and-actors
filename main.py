import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # CREATE
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

    genres = ["Western", "Action", "Dramma"]

    for name in genres:
        Genre.objects.create(name=name)
    # Genre.objects.create(name="Western")
    # Genre.objects.create(name="Action")
    # Genre.objects.create(name="Dramma")
    #
    # Actor.objects.create(first_name="George", last_name="Klooney")
    # Actor.objects.create(first_name="Kianu", last_name="Reeves")
    # Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    # Actor.objects.create(first_name="Will", last_name="Smith")
    # Actor.objects.create(first_name="Jaden", last_name="Smith")
    # Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # UPDATE
    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(first_name="George", last_name="Klooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
