import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = "Western", "Action", "Dramma"
    actors = [("George", "Kloone"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]

    for genre in genres:
        Genre.objects.create(name=genre)

    for name, surname in actors:
        Actor.objects.create(first_name=name, last_name=surname)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Kloone").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")
