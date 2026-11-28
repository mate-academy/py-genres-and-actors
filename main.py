import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma",
    ]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()

    clooney = Actor.objects.get(first_name="George", last_name="Klooney")
    clooney.last_name = "Clooney"
    clooney.save()

    reeves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    reeves.first_name = "Keanu"
    reeves.last_name = "Reeves"
    reeves.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")