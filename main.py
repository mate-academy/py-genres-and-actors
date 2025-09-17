
from django.db.models import QuerySet
from db.models import Actor
from db.models import Genre

def main() -> QuerySet:
    genre_to_add = ['Western', 'Action', 'Dramma']
    actors_to_add = [
        {
            'nombre':'George',
            'apellido':'Klooney'
        },
        {
            'nombre': 'Kianu',
            'apellido': 'Reaves'
        },
        {
            'nombre': 'Scarlett',
            'apellido': 'Keegan'
        },
        {
            'nombre': 'Will',
            'apellido': 'Smith'
        },{
            'nombre':'Jaden',
            'apellido':'Smith'
        },
        {
            'nombre': 'Scarlett',
            'apellido': 'Johansson'
        }

    ]
    for genre in genre_to_add:
        Genre.objects.create(name=genre)

    for actor in actors_to_add:
        Actor.objects.create(first_name=actor['nombre'], last_name=actor['apellido'])

    Genre.objects.filter(name='Dramma').update(name='Drama')
    Actor.objects.filter(first_name='George').update(last_name='Clooney')
    Actor.objects.filter(first_name='Kianu').update(first_name='Keanu', last_name='Reeves')
    Genre_to_delete = Genre.objects.get(name='Action')
    Genre_to_delete.delete()
    all_actresses_scarlet = Actor.objects.filter(first_name='Scarlett')
    all_actresses_scarlet.delete()


    return Actor.objects.filter(last_name='Smith').order_by("first_name")