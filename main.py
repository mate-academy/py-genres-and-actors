import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for name in genres:
        Genre.objects.create(name=name)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()
    actor = Actor.objects.get(last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()
    actor = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    genre = Genre.objects.get(name="Action")
    genre.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
