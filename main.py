import init_django_orm  # noqa: F401
from db.models import Actor, Genre

from django.db.models import QuerySet


def main() -> QuerySet:
    # CREATE
    for genre in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=genre)

    name = ["George", "Kianu", "Scarlett", "Will", "Jaden", "Scarlett"]
    last = ["Klooney", "Reaves", "Keegan", "Smith", "Smith", "Johansson"]

    for first_name, last_name in zip(name, last):
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # UPDATE
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")
