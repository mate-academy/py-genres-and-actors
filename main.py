import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Створення
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Drama")

    george = Actor.objects.create(first_name="George", last_name="Clooney")
    keanu = Actor.objects.create(first_name="Keanu", last_name="Reeves")
    scarlett = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(
        first_name="Scarlett", last_name="Johansson"
    )

    # Оновлення
    drama.name = "Drama"
    drama.save()

    george.last_name = "Clooney"
    george.save()

    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    # Видалення
    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Повернення QuerySet акторів із прізвищем Smith, впорядкованих за іменем
    actors_with_lastname_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return actors_with_lastname_smith
