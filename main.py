import init_django_orm  # noqa: F401

from django.db import models

from db.models import Actor, Genre

def create_obj(owner: type(models), **kwargs):
    owner.objects.create(**kwargs)

def main() -> models.QuerySet:

    new_genres = ["Western", "Action", "Dramma"]
    for genre in new_genres:
        create_obj(owner=Genre, name=genre)

    new_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first, last in new_actors:
        create_obj(owner=Actor, first_name=first, last_name=last)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    list_of_actors_updates = [
        [("George", "Klooney"), ("George", "Clooney")],
        [("Kianu", "Reaves"), ("Keanu", "Reeves")]
    ]
    for old_actor, new_actor in list_of_actors_updates:
        old_first, old_last = old_actor
        new_first, new_last = new_actor
        Actor.objects.filter(
            first_name=old_first, last_name=old_last
        ).update(first_name=new_first, last_name=new_last)

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    set_of_actors = Actor.objects.filter(
        last_name="Smith").order_by("first_name")
    return set_of_actors
