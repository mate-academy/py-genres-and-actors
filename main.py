import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre

actors = [
    "George Klooney",
    "Kianu Reaves",
    "Scarlett Keegan",
    "Will Smith",
    "Jaden Smith",
    "Scarlett Johansson"
]
genres = ["Western", "Action", "Dramma"]


def main() -> QuerySet:

    for actor_fn, actor_ln in actors.items:
        Actor.objects.create(first_name=actor_fn, last_name=actor_ln)

    for genre in genres:
        Genre.objects.create(name=genre)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(name="Scarlett").delete()
    Actor.objects.filter(last_name="Smith").all().order_by()
