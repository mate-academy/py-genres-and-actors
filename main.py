import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    # Створення жанрів
    genres_to_create = ["Western", "Action", "Dramma"]
    for genre_name in genres_to_create:
        Genre.objects.create(name=genre_name)

    # Створення акторів
    actors_to_create = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]
    for actor_data in actors_to_create:
        Actor.objects.create(**actor_data)

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
