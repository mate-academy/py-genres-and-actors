import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    george = Actor.objects.get(first_name="George", last_name="Klooney")
    george.last_name = "Clooney"
    george.save()
    keanu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    Actor.objects.filter(first_name="Scarlett").delete()

    Genre.objects.filter(name="Action").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
