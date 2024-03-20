import init_django_orm  # noqa: F401

from db.models import Genre, Actor

from django.db.models import QuerySet


def main() -> QuerySet:
    Genre.objects.create(
        name="Western",
    )
    Genre.objects.create(
        name="Action",
    )
    Genre.objects.create(
        name="Dramma",
    )
    Actor.objects.create(
        first_name="George",
        last_name="Klooney",
    )
    Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )

    drama_genre = Genre.objects.get(name="Dramma")
    drama_genre.name = "Drama"
    drama_genre.save()

    george = Actor.objects.get(last_name="Klooney")
    george.last_name = "Clooney"
    george.save()

    keanu = Actor.objects.get(first_name="Kianu")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
