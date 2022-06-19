import init_django_orm  # noqa: F401

from db.models import Genre
from db.models import Actor


def main():
    genger_list = ["Western", "Action", "Dramma"]
    actor_list = ["George Klooney", "Kianu Reaves",
                  "Scarlett Keegan", "Will Smith",
                  "Jaden Smith", "Scarlett Johansson"]
    for genger in genger_list:
        Genre.objects.create(name=genger)

    for actor in actor_list:
        name, second_name = actor.split()
        Actor.objects.create(first_name=name, last_name=second_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
