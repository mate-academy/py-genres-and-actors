import os
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    genre_western = Genre.objects.create(name="Western") # noqa
    genre_action = Genre.objects.create(name="Action")
    genre_drama = Genre.objects.create(name="Drama")

    actor_george_klooney = Actor.objects.create(
        first_name="George",
        last_name="Klooney"
    )
    actor_kianu_reaves = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves"
    )
    actress_scarlett_keegan = Actor.objects.create( # noqa
        first_name="Scarlett",
        last_name="Keegan"
    )
    actor_will_smith = Actor.objects.create( # noqa
        first_name="Will",
        last_name="Smith"
    )
    actor_jaden_smith = Actor.objects.create( # noqa
        first_name="Jaden",
        last_name="Smith"
    )
    actress_scarlett_johansson = Actor.objects.create( # noqa
        first_name="Scarlett",
        last_name="Johansson"
    )

    # Update
    genre_drama.name = "Drama"
    genre_drama.save()

    actor_george_klooney.last_name = "Clooney"
    actor_george_klooney.save()

    actor_kianu_reaves.first_name = "Keanu"
    actor_kianu_reaves.last_name = "Reeves"
    actor_kianu_reaves.save()

    # Delete
    genre_action.delete()

    actresses_scarlett = Actor.objects.filter(first_name="Scarlett")
    actresses_scarlett.delete()

    # Return
    actors_with_last_name_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return actors_with_last_name_smith


if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "py_genres_and_actors.settings"
    )
    main()
