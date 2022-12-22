import init_django_orm  # noqa: F401
from db.models import Actor, Genre
from django.db.models import QuerySet


def main() -> QuerySet:
    create_genre_western = Genre.objects.create(name="Western")  # noqa: F841
    create_genre_action = Genre.objects.create(name="Action")  # noqa: F841
    create_genre_dramma = Genre.objects.create(name="Dramma")  # noqa: F841
    create_actor_actress = Actor.objects.create(
        first_name="George", last_name="Klooney"
    )
    create_actor_actress = Actor.objects.create(
        first_name="Kianu", last_name="Reaves"
    )
    create_actor_actress = Actor.objects.create(
        first_name="Scarlett", last_name="Keegan"
    )
    create_actor_actress = Actor.objects.create(
        first_name="Will", last_name="Smith"
    )
    create_actor_actress = Actor.objects.create(
        first_name="Jaden", last_name="Smith"
    )
    create_actor_actress = Actor.objects.create(  # noqa: F841
        first_name="Scarlett", last_name="Johansson"
    )

    filter_genre = Genre.objects.filter(  # noqa: F841
        name="Dramma"
    ).update(name="Drama")
    filter_actor_last_name = Actor.objects.filter(  # noqa: F841
        last_name="Klooney"
    ).update(last_name="Clooney")
    filter_actor_first_name = Actor.objects.filter(  # noqa: F841
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")
    del_genre_action = Genre.objects.filter(  # noqa: F841
        name="Action"
    ).delete()
    del_name_scarlett = Actor.objects.filter(  # noqa: F841
        first_name="Scarlett"
    ).delete()
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")


if __name__ == '__main__':  # noqa: Q000
    main()
