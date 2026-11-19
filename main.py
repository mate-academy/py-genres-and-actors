import init_django_orm  # noqa: F401
from db.models import Actor, Genre
from django.db.models import QuerySet


def main() -> QuerySet:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]
    for name, in genres:
        Genre.objects.create(name=name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()

    george_klooney = Actor.objects.get(
        first_name="George", last_name="Klooney")
    george_klooney.last_name = "Clooney"
    george_klooney.save()

    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    action = Genre.objects.get(name="Action")
    action.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    smitt = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smitt
