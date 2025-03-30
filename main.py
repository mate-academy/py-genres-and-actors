import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")

    george_klooney = Actor.objects.create(first_name="George", last_name="Klooney")
    keanu_reeves = Actor.objects.create(first_name="Keanu", last_name="Reeves")
    scarlett_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    drama.name = "Drama"
    drama.save()

    george_klooney.last_name = "Clooney"
    george_klooney.save()

    keanu_reeves.first_name = "Keanu"
    keanu_reeves.last_name = "Reeves"
    keanu_reeves.save()

    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(last_name="Smith").order_by('first_name')

    return smith_actors
