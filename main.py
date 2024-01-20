import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres_data = ["Western", "Action", "Drama"]
    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    genres = [Genre.objects.create(name=genre_name) for genre_name
              in genres_data]
    actors = [Actor.objects.create(first_name=first_name, last_name=last_name) 
              for first_name, last_name in actors_data]
    genres[-1].name = "Drama"
    genres[-1].save()
    actors[0].last_name = "Clooney"
    actors[1].first_name = "Keanu"
    actors[1].last_name = "Reeves"
    [actor.save() for actor in actors[:2]]
    genres[1].delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    queryset = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return queryset
