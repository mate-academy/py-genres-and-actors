import init_django_orm
from db.models import Genre, Actor# noqa: F401

from django.db.models import QuerySet


def main() -> QuerySet:
    for i in ["Western", "Action", "Dramma"]:
        genre = Genre(name = i)
        genre.save()


    for i in [("George", "Klooney"),
         ("Kianu", "Reaves"),
         ("Scarlett", "Keegan"),
         ("Will", "Smith"),
         ("Jaden", "Smith"),
         ("Scarlett", "Johansson")]:
        first_name, last_name = i
        actor = Actor(
            first_name = first_name,
            last_name = last_name
        )
        actor.save()

    filtered_genres = Genre.objects.filter(
        name = "Dramma"
    ).update(name = "Drama")

    filtered_actors = Actor.objects.filter(
        last_name = "Klooney").update(last_name = "Clooney")

    filtered_actors = Actor.objects.filter(
        first_name = "Kianu").update(first_name = "Keanu")

    filtered_actors = Actor.objects.filter(
        last_name = "Reaves").update(last_name = "Reeves")

    filtered_genres = Genre.objects.filter(
        name = "Action"
    ).delete()

    filtered_actors = Actor.objects.filter(
        first_name = "Scarlett"
    ).delete()

    result = Actor.objects.filter(last_name = "Smith").order_by("first_name")
    return result