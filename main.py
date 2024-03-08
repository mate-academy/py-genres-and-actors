import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Ganre, Actor


def main() -> QuerySet:
    Ganre.objects.create(name="Western")
    Ganre.objects.create(name="Action")
    Ganre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name='Kianu', last_name='Reaves')
    Actor.objects.create(first_name='Scarlett', last_name='Keegan')
    Actor.objects.create(first_name='Will', last_name='Smith')
    Actor.objects.create(first_name='Jaden', last_name='Smith')
    Actor.objects.create(first_name='Scarlett', last_name='Johansson')

    Ganre.objects.filter(name='Dramma').update(name='Drama')
    Actor.objects.filter(first_name='George', last_name='Klooney').update(
        last_name='Clooney')
    Actor.objects.filter(first_name='Kianu', last_name='Reaves').update(
        first_name='Keanu', last_name='Reeves')

    Ganre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name='Scarlett').delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
