from django.template.defaultfilters import first

import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main():
    genres = ['Western', 'Action', 'Dramma']
    actors = [
        ('George', 'Klooney'),
        ('Kianu', 'Reaves'),
        ('Scarlett', 'Keegan'),
        ('Will', 'Smith'),
        ('Jaden', 'Smith'),
        ('Scarlett', 'Johansson'),
    ]

    genres_to_update = [('Dramma', 'Drama')]

    actors_last_name_to_update = [
        ('Klooney', 'Clooney'),
        ('Reaves', 'Reeves'),
    ]

    actors_first_name_to_update = [('Kianu', 'Keanu')]
    genres_to_delete = ['Action']
    actors_first_name_to_delete = ['Scarlett']

    # CREATE
    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # UPDATE
    for from_, to_ in genres_to_update:
        Genre.objects.filter(name=from_).update(name=to_)

    for from_, to_ in actors_last_name_to_update:
        Actor.objects.filter(last_name=from_).update(last_name=to_)

    for from_, to_ in actors_first_name_to_update:
        Actor.objects.filter(first_name=from_).update(first_name=to_)

    # DELETE
    for genre_to_delete in genres_to_delete:
        Genre.objects.filter(name=genre_to_delete).delete()

    for actor_to_delete in actors_first_name_to_delete:
        Actor.objects.filter(first_name=actor_to_delete).delete()


    return Actor.objects.filter(last_name='Smith').order_by('first_name')


if __name__ == '__main__':
    query_set = main()
    print(query_set)
