import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:

    new_genres = ["Western", "Action", "Dramma"]
    for genre in new_genres:
        Genre.objects.create(name=genre)

    new_actors = ["George Klooney", "Kianu Reaves",
                  "Scarlett Keegan", "Will Smith",
                  "Jaden Smith", "Scarlett Johansson"]
    for actor in new_actors:
        first, last = actor.split(" ")
        Actor.objects.create(first_name=first, last_name=last)

    list_of_genres_updates = [("Dramma", "Drama")]
    for old_genre, new_genre in list_of_genres_updates:
        Genre.objects.filter(name=old_genre).update(name=new_genre)

    list_of_actors_updates = [("George Klooney", "George Clooney"),
                              ("Kianu Reaves", "Keanu Reeves")]
    for old_actor, new_actor in list_of_actors_updates:
        old_first, old_last = old_actor.split(" ")
        new_first, new_last = new_actor.split(" ")
        Actor.objects.filter(
            first_name=old_first, last_name=old_last
        ).update(first_name=new_first, last_name=new_last)

    Genre.objects.filter(name="Drama").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    set_of_actors = Actor.objects.filter(
        last_name="Smith").order_by("first_name")
    return set_of_actors
