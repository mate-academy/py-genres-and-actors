import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        final_genre = Genre(name=genre)
        final_genre.save()
    actors = [("George", "Klooney"), ("Kianu", "Reaves"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Keegan") ,
              ("Scarlett", "Johansson")]
    for fn, ln in actors:
        final_actor = Actor(
            first_name=fn, last_name=ln)
        final_actor.save()
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
