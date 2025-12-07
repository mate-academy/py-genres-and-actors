import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Dramma"]
    for genre_data in genres_to_create:
        Genre.objects.create(name=genre_data)

    first_and_last_name = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for name in first_and_last_name:
        Actor.objects.create(first_name=name[0], last_name=name[1])

    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()
    george_klooney = Actor.objects.get(
        first_name="George", last_name="Klooney"
    )
    george_klooney.last_name = "Clooney"
    george_klooney.save()
    kianu_reaves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu_reaves.first_name = "Keanu"
    kianu_reaves.last_name = "Reeves"
    kianu_reaves.save()
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    smith_actors_queryset = Actor.objects.filter(
        last_name="Smith").order_by("first_name")
    return smith_actors_queryset
