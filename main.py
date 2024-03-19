import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    # Створення жанрів
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    # Створення акторів
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Оновлення жанру "Dramma" на "Drama"
    Genre.objects.filter(name="Dramma").update(name="Drama")
    # Оновлення актора "George Klooney" на "George Clooney"
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    # Оновлення актора "Kianu Reaves" на "Keanu Reeves"
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # Видалення жанру "Action"
    Genre.objects.filter(name="Action").delete()
    # Видалення всіх актрис з ім'ям "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # Повернення QuerySet акторів з фамілією "Smith" та впорядкованих за ім'ям
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    actors_with_smith_last_name = main()
    print(actors_with_smith_last_name)
    print(Genre.objects.all())
    print(Actor.objects.all())
