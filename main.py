import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main():
    # Create genres
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")

    # Create actors and actresses
    george = Actor.objects.create(first_name="George", last_name="Klooney")
    keanu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Update genre and actor details
    drama.name = "Drama"
    drama.save()

    george.last_name = "Clooney"
    george.save()

    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    # Delete genre and actresses
    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return actors with last name 'Smith', ordered by first_name
    actors_with_smith = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return actors_with_smith
