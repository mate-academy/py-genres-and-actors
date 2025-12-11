import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_data = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]
    for (name,) in genre_data:
        Genre.objects.create(name=name)
    print(Genre.objects.all())

    actor_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actor_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)
    print(Actor.objects.all())

    Genre.objects.filter(name="Dramma").update(name="Drama")

    for actor in Actor.objects.filter(last_name="Klooney"):
        actor.last_name = "Clooney"
        actor.save()

    for actor in Actor.objects.filter(first_name="Kianu", last_name="Reaves"):
        actor.first_name = "Keanu"
        actor.last_name = "Reeves"
        actor.save()

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors
