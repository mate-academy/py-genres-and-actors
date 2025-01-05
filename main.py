import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Keanu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    # Create
    for genre in genres:
        Genre.objects.create(name=genre)
    for actor_first_name, actor_last_name in actors:
        Actor.objects.create(
            first_name=actor_first_name,
            last_name=actor_last_name
        )
    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")
    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    # Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
