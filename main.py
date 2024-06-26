import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Artist


def main() -> QuerySet:
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")

    klooney = Artist.objects.create(first_name="George", last_name="Klooney")
    reaves = Artist.objects.create(first_name="Kianu", last_name="Reaves")
    keegan = Artist.objects.create(first_name="Scarlett", last_name="Keegan")
    smith_will = Artist.objects.create(first_name="Will", last_name="Smith")
    smith_jaden = Artist.objects.create(first_name="Jaden", last_name="Smith")
    johansson = Artist.objects.create(first_name="Scarlett", last_name="Johansson")

    drama.name = "Drama"
    drama.save()

    klooney.last_name = "Clooney"
    klooney.save()

    reaves.first_name = "Keanu"
    reaves.last_name = "Reaves"
    reaves.save()

    action.delete()
    Artist.objects.filter(first_name="Scarlett").delete()

    smith_actors = Artist.objects.filter(last_name="Smith").order_by("first_name")
    return smith_actors
