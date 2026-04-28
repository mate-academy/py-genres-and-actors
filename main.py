import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres_to_create = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]
    actors_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for (name,) in genres_to_create:
        Genre.objects.create(name=name)

    for first_name, last_name in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    drama_genre = Genre.objects.get(name="Dramma")
    drama_genre.name = "Drama"
    drama_genre.save()

    george_clooney = Actor.objects.get(
        first_name="George",
        last_name="Klooney",
    )
    george_clooney.last_name = "Clooney"
    george_clooney.save()

    keanu_reeves = Actor.objects.get(
        first_name="Kianu",
        last_name="Reaves",
    )
    keanu_reeves.first_name = "Keanu"
    keanu_reeves.last_name = "Reeves"
    keanu_reeves.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
