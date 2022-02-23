import init_django_orm  # noqa: F401


from db.models import Genre, Actor


def main():
    genres_to_create = [
        'Western',
        'Action',
        'Dramma',
    ]
    actors_to_create = [
        'Kianu Reaves',
        'Scarlett Keegan',
        'Will Smith',
        'Jaden Smith',
        'Scarlett Johansson',
    ]
    for genre in genres_to_create:
        Genre.objects.create(
            name=genre
        )

    for actor in actors_to_create:
        first_name, last_name = actor.split()
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    Genre.objects.filter(
        name='Dramma'
    ).update(name='Drama')

    Actor.objects.filter(
        first_name='George',
        last_name='Klooney',
    ).update(last_name='Clooney')

    Actor.objects.filter(
        first_name='Kianu',
        last_name='Reaves',
    ).update(last_name='Reeves')

    Genre.objects.filter(
        name='Actor'
    ).delete()

    Actor.object.filter(
        first_name='Scarlett'
    ).delete()

    return Actor.objects.filter(
        last_name='Smith'
    ).order_by('first_name')
