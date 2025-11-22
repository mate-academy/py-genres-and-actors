import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlet", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlet", "Johansson"),
    ]

    for name in genres:
        Genre.objects.create(name=name)

    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves")

    deletes = [
        Genre.objects.filter(name="Action"),
        Actor.objects.filter(first_name="Scarlet"),
    ]

    for queryset in deletes:
        queryset.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
