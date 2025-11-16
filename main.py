import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        final_genre = Genre(name=genre)
        final_genre.save()
    actors = ["George Klooney", "Kianu Reaves", "Will Smith", "Jaden Smith"]
    for actor in actors:
        actor = actor.split()
        final_actor = Actor(
            first_name=actor[0], last_name=actor[1])
        final_actor.save()
    actresses = ["Scarlett Keegan" , "Scarlett Johansson"]
    for actress in actresses:
        actress = actress.split()
        final_actress = (Actor(first_name=actress[0],
                               last_name=actress[1]
                               )
                         )
        final_actress.save()
    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves")
    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
