import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "klooney"), ("Kianu", "Reaves"), ("Scarlett", "Keegan"),
        ("Will", "Smith"), ("Jaden", "Smith"), ("Scarlett", "Johansson")
    ]

    for actor in actors:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        last_name="Reeves",
        first_name="Keanu"
    )

    acao = Genre.objects.filter(name="Action")
    acao.delete()
    widow = Actor.objects.filter(first_name="Scarlett")
    widow.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
