import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    add_genres_western = Genre.objects.create(
        name="Western",
    )
    print(add_genres_western)

    add_genres_action = Genre.objects.create(
        name="Action",
    )
    print(add_genres_action)

    add_genres_dramma = Genre.objects.create(
        name="Dramma",
    )
    print(add_genres_dramma)

    add_actors_klooney = Actor.objects.create(
        first_name="George",
        last_name="Klooney",
    )
    print(add_actors_klooney)

    add_actors_reaves = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves",
    )
    print(add_actors_reaves)

    add_actors_keegan = Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    print(add_actors_keegan)

    add_actors_smith_w = Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    print(add_actors_smith_w)

    add_actors_smith_j = Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    print(add_actors_smith_j)

    add_actors_johansson = Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )
    print(add_actors_johansson)

    update_genres_drama = Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    print(update_genres_drama)

    update_actors_clooney = Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")
    print(update_actors_clooney)

    update_actors_reeves = Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(
        first_name="Keanu",
        last_name="Reeves",
    )
    print(update_actors_reeves)

    delete_genres_action = Genre.objects.filter(
        name="Action",
    ).delete()
    print(delete_genres_action)

    delete_actors_scarlett = Actor.objects.filter(
        first_name="Scarlett",
    ).delete()
    print(delete_actors_scarlett)

    sort_actor = Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
    print(sort_actor)
    return sort_actor
