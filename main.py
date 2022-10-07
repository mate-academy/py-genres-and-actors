import init_django_orm  # noqa: F401
from db.models import Actor, Genre
from django.db.models import QuerySet

from django.db.models import QuerySet


def main() -> QuerySet:
    new_genre_western = Genre.objects.create(name="Western")
    new_genre_action = Genre.objects.create(name="Action")
    new_genre_dramma = Genre.objects.create(name="Dramma")

    new_actor = Actor.objects.create(
        first_name="George",
        last_name="Klooney",
    )
    new_actor = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves",
    )
    new_actress = Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    new_actor = Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    new_actor = Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    new_actress = Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )
    update_genre_dramma_to_darma = Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    update_actor_kloony_last_name = Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")
    update_actor_keanu_firstandlast_name = Actor.objects.filter(
        first_name="Kianu", last_name="Reaves",
    ).update(first_name="Keanu", last_name="Reeves")
    delete_genre_action = Genre.objects.filter(
        name="Action"
    ).delete()
    delete_all_actress_scarlett = Actor.objects.filter(
        first_name="Scarlett"
    ).delete()
    return_queryset_with_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return return_queryset_with_smith
