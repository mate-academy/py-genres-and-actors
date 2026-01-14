import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ("Western", "Action", "Dramma")
    genre_obj = Genre.objects
    for genre in genres:
        genre_obj.create(name=genre)
    actors = (
        ("George", "Klooney"), ("Kianu", "Reaves"), ("Scarlett", "Keegan"),
        ("Will", "Smith"), ("Jaden", "Smith"), ("Scarlett", "Johansson")
    )
    actor_obj = Actor.objects
    for first_name_, last_name_ in actors:
        actor_obj.create(first_name=first_name_, last_name=last_name_)
    obj = genre_obj.get(name="Dramma")
    obj.name = "Drama"
    obj.save()
    obj = actor_obj.get(first_name="George", last_name="Klooney")
    obj.last_name = "Clooney"
    obj.save()
    obj = actor_obj.get(first_name="Kianu", last_name="Reaves")
    obj.first_name = "Keanu"
    obj.last_name = "Reeves"
    obj.save()
    genre_obj.get(name="Action").delete()
    delete_obj = actor_obj.filter(first_name="Scarlett")
    for obj in delete_obj:
        obj.delete()
    return actor_obj.filter(last_name="Smith").order_by("first_name")
