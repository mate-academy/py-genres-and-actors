import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()


def main() -> QuerySet:
    # Create genres
    genre_names = ["Western", "Action", "Dramma"]
    genres = {name: Genre.objects.create(name=name) for name in genre_names}

    dramma = genres["Dramma"]

    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Update operations
    dramma.name = "Drama"
    dramma.save()

    george = (Actor.objects.
              get(first_name="George"))  # тепер потрібна змінна для оновлення
    george.last_name = "Clooney"
    george.save()

    keanu = Actor.objects.get(first_name="Kianu")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    # Delete operations
    action = Genre.objects.get(name="Action")
    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return queryset of actors with last_name "Smith" ordered by first_name
    result = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return result
