import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    # --- Create genres ---
    genres = ["Western", "Action", "Dramma"]
    for name in genres:
        Genre.objects.create(name=name)

    # --- Update genres ---
    genre = Genre.objects.filter(name="Dramma").first()
    if genre:
        genre.name = "Drama"
        genre.save()

    # --- Delete genres ---
    Genre.objects.filter(name="Action").delete()

    # --- Create actors ---
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    # --- Update actors ---
    george = Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).first()
    if george:
        george.last_name = "Clooney"
        george.save()

    keanu = Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).first()
    if keanu:
        keanu.first_name = "Keanu"
        keanu.last_name = "Reeves"
        keanu.save()

    # --- Delete actors ---
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
