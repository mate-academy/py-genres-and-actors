import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import *


def main() -> QuerySet:
    for genre_ in ('Western', 'Action', 'Dramma'):
        genre = Genre.objects.create(name=genre_)
    for first_name, last_name in (['George', 'Klooney'], ['Kianu', 'Reaves'], ['Scarlett', 'Keegan'],
                   ['Will', 'Smith'], ['Jaden', 'Smith'], ['Scarlett', 'Johansson']):
        actor = Actor.objects.create(first_name=first_name, last_name=last_name)
    Genre.objects.filter(name='Dramma').update(name='Drama')
    Actor.objects.filter(last_name='Klooney').update(last_name='Clooney')
    Actor.objects.filter(first_name='Kianu').update(first_name='Keanu', last_name='Reeves')
    Genre.objects.get(name='Action').delete()
    Actor.objects.filter(first_name='Scarlett').delete()
    return Actor.objects.filter(last_name='Smith').order_by('first_name')
