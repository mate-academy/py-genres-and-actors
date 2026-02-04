import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Actor, Genre


genres = [
    "Western",
    "Action",
    "Dramma"
]

actors = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def main() -> QuerySet:
    # Create
    for genre_name in genres:
        Genre.objects.create(name=genre_name)
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu",
                                                    last_name="Reeves")

    # Delete
    genre = Genre.objects.get(name="Action")
    genre.delete()

    actress = Actor.objects.filter(first_name="Scarlett")
    actress.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
