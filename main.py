import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    ganres = ["Western", "Action", "Dramma"]
    actors = ["George Klooney",
              "Kianu Reaves",
              "Scarlett Keegan",
              "Will Smith",
              "Jaden Smith",
              "Scarlett Johansson"
              ]

    for genre in ganres:
        genre_create = Genre.objects.create(name=genre)
        print(genre_create)

    for actor in actors:
        first_name, last_name = actor.split(" ", 1)
        actors_create = Actor.objects.create(
            first_name=first_name,
            last_name=last_name)
        print(actors_create)

        filtered_genres = Genre.objects.filter(
            name="Dramma",).update(name="Drama",)
        print(filtered_genres)

        Genre.objects.filter(name="Action").delete()
        Actor.objects.filter(first_name="Scarlett").delete()

        smith_actors = Actor.objects.filter(
            last_name="Smith").order_by("first_name")
        return smith_actors
