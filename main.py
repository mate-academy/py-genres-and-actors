import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # 1. Створення жанрів через цикл
    genres = [
        ("Western",),
        ("Action",),
        ("Drama",),
    ]
    for (name,) in genres:
        Genre.objects.create(name=name)

    # 2. Створення акторів через цикл
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reeves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # 3. Оновлення записів
    Genre.objects.filter(name="Drama").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reeves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # 4. Видалення записів
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 5. Повернення відфільтрованого та відсортованого QuerySet
    return Actor.objects.filter(last_name="Smith").order_by("first_name")