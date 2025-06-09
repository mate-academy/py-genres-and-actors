import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")
    george = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    drama.name = "Drama"
    drama.save()
    george.last_name = "Clooney"
    george.save()
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    queryset = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return queryset
