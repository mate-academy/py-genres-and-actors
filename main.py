import init_django_orm  # noqa: F401
from db.models import Genre, Actor

from django.db.models import QuerySet


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for item in genres:
        Genre.objects.create(name=item)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for name, surname in actors:
        Actor.objects.create(first_name=name, last_name=surname)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")
