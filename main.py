import os
import django


# Указываем путь к настройкам Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

# Импорт моделей
from db.models import Genre, Actor


def main() -> list[tuple[str, str]]:

    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    # Создание актеров (исправленные имена и фамилии)
    Actor.objects.create(first_name="George", last_name="Clooney")
    # Исправлено на "Clooney"
    Actor.objects.create(first_name="Keanu", last_name="Reeves")
    # Исправлено на "Keanu Reeves"
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    # Исправлено на "Will"
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    # Исправлено на "Jaden"
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Обновление жанра "Dramma" → "Drama"
    genre_drama = Genre.objects.get(name="Dramma")
    genre_drama.name = "Drama"
    genre_drama.save()

    # Удаление жанра "Action"
    Genre.objects.filter(name="Action").delete()

    # Удаление всех актеров с именем "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # Возврат QuerySet с методом values_list()
    smith_actors = (Actor.objects.filter(last_name="Smith")
                    .order_by("first_name"))
    return smith_actors.values_list("first_name", "last_name")


if __name__ == "__main__":
    result = main()
    print(result)
