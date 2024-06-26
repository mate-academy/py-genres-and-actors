import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]

    genre_objects = []
    for genre_name in genres:
        genre_objects.append(Genre.objects.create(name=genre_name))

    actor_objects = []
    for actor_data in actors:
        actor_objects.append(Actor.objects.create(**actor_data))

    drama_genre = Genre.objects.get(name="Dramma")
    drama_genre.name = "Drama"
    drama_genre.save()

    klooney_actor = Actor.objects.get(first_name="George", last_name="Klooney")
    klooney_actor.last_name = "Clooney"
    klooney_actor.save()

    reaves_actor = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    reaves_actor.first_name = "Keanu"
    reaves_actor.last_name = "Reeves"
    reaves_actor.save()

    Genre.objects.get(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(last_name="Smith") \
        .order_by("first_name")
    return smith_actors
