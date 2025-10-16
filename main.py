from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    initial_genres = ["Western", "Action", "Dramma"]
    for genre_name in initial_genres:
        Genre.objects.get_or_create(name=genre_name)

    # --- Оновлення та видалення жанрів ---
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Genre.objects.filter(name="Action").delete()

    # --- Створення початкових акторів ---
    initial_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reeves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in initial_actors:
        Actor.objects.get_or_create(first_name=first_name, last_name=last_name)

    # --- Оновлення помилок у іменах ---
    Actor.objects.filter(first_name="George",
                         last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu",
                         last_name="Reeves").update(first_name="Keanu",
                                                    last_name="Reeves")

    # --- Видалення акторів ---
    Actor.objects.filter(first_name="Scarlett").delete()

    # --- Повернення акторів із прізвищем 'Smith', відсортованих по імені ---
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
