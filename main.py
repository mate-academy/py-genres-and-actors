import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:

    genres = (
        "Western", "Action", "Dramma"
    )

    for genre in genres:
        Genre.objects.create(name=genre)

    actors = (
        "George Klooney", "Kianu Reaves",
        "Scarlett Keegan", "Will Smith",
        "Jaden Smith", "Scarlett Johansson"
    )

    full_names = [name.split() for name in actors]

    for first_name, last_name in full_names:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
