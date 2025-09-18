import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]

    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    george_clooney = Actor.objects.get(last_name="Klooney")
    george_clooney.last_name = "Clooney"
    george_clooney.save()
    keanu = Actor.objects.get(first_name="Kianu")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
