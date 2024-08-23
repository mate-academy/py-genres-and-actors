import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Clooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    actor_name = Actor.objects.get(first_name="George", last_name="Clooney")
    actor_name.second_name = "Clooney"
    actor_name.save()

    actor = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    new_query = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return new_query
