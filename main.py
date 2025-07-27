import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    create_genres = Genre.objects.bulk_create(
        [
            Genre(name="Western"),
            Genre(name="Action"),
            Genre(name="Dramma")
        ]
    )
    create_actors = Actor.objects.bulk_create(
        [
            Actor(first_name="George", last_name="Klooney"),
            Actor(first_name="Kianu", last_name="Reaves"),
            Actor(first_name="Scarlett", last_name="Keegan"),
            Actor(first_name="Will", last_name="Smith"),
            Actor(first_name="Jaden", last_name="Smith"),
            Actor(first_name="Scarlett", last_name="Johansson")
        ]
    )

    update_dramma = Genre.objects.filter(name="Dramma").update(name="Drama")
    update_klooney = Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney"
    )
    update_kianu = Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    delete_action = Genre.objects.filter(name="Action").delete()
    delete_scarlett = Actor.objects.filter(first_name="Scarlett").delete()

    print(
        create_genres,
        create_actors,
        update_dramma,
        update_klooney,
        update_kianu,
        delete_action,
        delete_scarlett
    )

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
