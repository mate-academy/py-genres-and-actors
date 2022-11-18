import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Actor, Genre   # noqa: F401


def main() -> QuerySet:
    for genre in ("Western", "Action", "Dramma"):
        Genre.objects.create(
            name=genre,
        )
    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]
    for first, last in actors:
        Actor.objects.create(
            first_name=first,
            last_name=last
        )

    Genre.objects.filter(name="Dramma", ).update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action", ).delete()
    Actor.objects.filter(first_name="Scarlett", ).delete()
    return Actor.objects.filter(last_name="Smith",).order_by("first_name")
