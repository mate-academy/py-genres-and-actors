import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor
from db.models import Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George Klooney"), ("Kianu Reaves"),
              ("Scarlett Keegan"), ("Will Smith"),
              ("Jaden Smith"), ("Scarlett Johansson")]
    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        first_name, last_name = actor.split(" ")
        Actor.objects.create(first_name=first_name,
                             last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(last_name="Klooney").
     update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu").
     update(first_name="Keanu", last_name="Reeves"))

    action_genre = Genre.objects.filter(name="Action")
    if action_genre.exists():
        action_genre.delete()

    actress_scarlett = Actor.objects.filter(first_name="Scarlett")
    if actress_scarlett.exists():
        actress_scarlett.delete()

    sorted_actors = (Actor.objects.
                     filter(last_name="Smith").
                     order_by("first_name"))
    return sorted_actors
