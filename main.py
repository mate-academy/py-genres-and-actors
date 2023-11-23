import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Update
    drama_genre = Genre.objects.get(name="Dramma")
    drama_genre.name = "Drama"
    drama_genre.save()

    george_klooney = Actor.objects.get(
        first_name="George", last_name="Klooney"
    )
    george_klooney.last_name = "Clooney"
    george_klooney.save()

    kianu_reaves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu_reaves.first_name = "Keanu"
    kianu_reaves.last_name = "Reeves"
    kianu_reaves.save()

    # Delete
    action_genre = Genre.objects.get(name="Action")
    action_genre.delete()

    actresses_scarlett = Actor.objects.filter(first_name="Scarlett")
    actresses_scarlett.delete()

    # Return
    actors_smith = Actor.objects.filter(
        last_name="Smith").order_by("first_name")
    return actors_smith
