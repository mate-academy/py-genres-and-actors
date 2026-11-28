import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


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

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
