import init_django_orm  # noqa: F401

from django.db.models import QuerySet


from db.models import Actor, Genre


def main() -> QuerySet:
    genress = [
        Genre(name=name)
        for name in (
            "Western",
            "Action",
            "Dramma",
        )
    ]
    if Genre.objects.count() != 0:
        Genre.objects.all().delete()
    Genre.objects.bulk_create(genress)

    actors = [
        Actor(first_name=first_name, last_name=last_name)
        for first_name, last_name in [
            ("George", "Klooney"),
            ("Kianu", "Reaves"),
            ("Scarlett", "Keegan"),
            ("Will", "Smith"),
            ("Jaden", "Smith"),
            ("Scarlett", "Johansson"),
        ]
    ]
    if Actor.objects.count() != 0:
        Actor.objects.all().delete()
    Actor.objects.bulk_create(actors)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
