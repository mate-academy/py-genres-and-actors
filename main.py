import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres_data = [("Western",), ("Action",), ("Drama",)]
    Genre.objects.bulk_create([Genre(name=name) for name, in genres_data])

    actors_data = [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
    ]
    Actor.objects.bulk_create([Actor(first_name=fn, last_name=ln)
                               for fn, ln in actors_data])

    genre_dramma = Genre.objects.filter(name="Dramma").first()
    if genre_dramma:
        genre_dramma.name = "Drama"
        genre_dramma.save()

    Actor.objects.filter(first_name="George", last_name="Klooney")\
        .update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves")\
        .update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    ordered_actors = Actor.objects.filter(last_name="Smith")\
        .order_by("first_name")

    return ordered_actors
