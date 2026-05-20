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

    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save(update_fields=["name"])

    clooney = Actor.objects.get(first_name="George", last_name="Klooney")
    clooney.last_name = "Clooney"
    clooney.save(update_fields=["last_name"])

    jhonny = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    jhonny.first_name = "Keanu"
    jhonny.last_name = "Reeves"
    jhonny.save(update_fields=["first_name", "last_name"])

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
