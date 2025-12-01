import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


genres_ls = ["Western", "Action", "Dramma"]
actors_ls = [("George", "Klooney"), ("Kianu", "Reaves"),
             ("Scarlett", "Keegan"), ("Will", "Smith"),
             ("Jaden", "Smith"), ("Scarlett", "Johansson")]


def main() -> QuerySet:
    for genre in genres_ls:
        Genre.objects.create(name=genre)

    for (name, surname) in actors_ls:
        Actor.objects.create(first_name=name, last_name=surname)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(
        first_name="George", last_name="Clooney"
    )

    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action",).delete()

    Actor.objects.filter(first_name="Scarlett",).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
