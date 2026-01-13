import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western",
              "Action",
              "Dramma"]

    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]

    for genre in genres:
        Genre.objects.create(name=genre)
    for first_name, lastname in actors:
        Actor.objects.create(first_name=first_name, last_name=lastname)

    Genre.objects.filter(name="Dramma").update(
        name="Drama"
    )
    Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(
        last_name="Reaves", first_name="Kianu"
    ).update(
        last_name="Reeves", first_name="Keanu"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
