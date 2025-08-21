import os
import django
from django.db.models import QuerySet

# noqa: E402 because Django requires setup before importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema.settings")
django.setup()

from db.models import Genre, Actor  # noqa: E402


def main() -> QuerySet[Actor]:
    """Main function that creates, updates, deletes and returns actors."""

    # Tworzenie gatunków filmowych
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    # Tworzenie aktorów/aktorek
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Aktualizacje
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # Usuwanie
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Zwracanie aktorów o nazwisku "Smith", posortowanych po imieniu
    smiths = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smiths


if __name__ == "__main__":
    result = main()
    for actor in result:
        print(actor)
