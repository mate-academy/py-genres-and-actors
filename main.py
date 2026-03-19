import init_django_orm  # noqa: F401
import django

from django.db.models import QuerySet
from db.models import Genre, Actor

django.setup()


def main() -> QuerySet:

    # 1. CREATE
    genres = ["Western", "Action", "Dramma"]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    # 2. UPDATE
    dramma_genre = Genre.objects.get(name="Dramma")
    dramma_genre.name = "Drama"
    dramma_genre.save()

    george = Actor.objects.get(first_name="George", last_name="Klooney")
    george.last_name = "Clooney"
    george.save()

    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    # 3. DELETE
    action_genre = Genre.objects.get(name="Action")
    action_genre.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. RETURN
    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    )
    return smith_actors
