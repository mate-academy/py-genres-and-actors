from django.db.models import QuerySet

from db.models import Genre, Actor

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()


def main() -> QuerySet:
    # Create genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")  # треба для оновлення

    # Create actors/actresses
    (Actor.objects.
     create(first_name="George", last_name="Klooney"))  # змінна не потрібна
    (Actor.objects.
     create(first_name="Kianu", last_name="Reaves"))  # змінна не потрібна
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

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


if __name__ == "__main__":
    qs = main()
    print(qs)
    print(Genre.objects.all())
    print(Actor.objects.all())
