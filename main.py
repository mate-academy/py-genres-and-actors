import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for item in genres:
        Genre.objects.create(
            name=item
        )
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_item, second_item in actors:
        Actor.objects.create(
            first_name=first_item,
            last_name=second_item
        )

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    clooney = Actor.objects.get(last_name="Klooney")
    clooney.last_name = "Clooney"
    clooney.save()

    kianu = Actor.objects.get(first_name="Kianu")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    Genre.objects.filter(name="Action").delete()

    scarlett = Actor.objects.filter(first_name="Scarlett")
    scarlett.delete()

    smith = Actor.objects.filter(last_name="Smith")
    return smith.order_by("first_name")
