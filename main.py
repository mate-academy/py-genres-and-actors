import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genre_for_creating = ["Western", "Action", "Dramma"]

    actors_for_creating = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for name_of_genre in genre_for_creating:
        Genre.objects.create(name=name_of_genre)

    for first_name, last_name in actors_for_creating:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
