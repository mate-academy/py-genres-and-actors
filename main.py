import os
import sys
from typing import Any

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django  # noqa: E402
django.setup()  # noqa: E402

from db.models import Actor, Genre  # noqa: E402


def main() -> Any:
    Genre.objects.all().delete()
    Actor.objects.all().delete()

    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    result = main()

    print("Resultado dos atores com sobrenome Smith:")
    for actor in result:
        print(f"{actor.first_name} {actor.last_name}")

    print("\nGêneros restantes:")
    for genre in Genre.objects.all():
        print(genre.name)

    print("\nTodos os atores restantes:")
    for actor in Actor.objects.all():
        print(f"{actor.first_name} {actor.last_name}")
