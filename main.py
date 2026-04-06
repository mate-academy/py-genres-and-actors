import os
import django
from typing import Any

from db.models import Actor, Genre


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main() -> Any:
    # limpar dados (evita duplicação)
    Genre.objects.all().delete()
    Actor.objects.all().delete()

    # CREATE
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # UPDATE
    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    result = main()

    print(result)
    print(Genre.objects.all())
    print(Actor.objects.all())
