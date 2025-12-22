import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genre_names = ["Western", "Action", "Dramma"]
    actor_names = ["George", "Kianu", "Scarlett", "Will", "Jaden", "Scarlett"]
    actor_surnames = [
        "Klooney", "Reaves", "Keegan", "Smith", "Smith", "Johansson"
    ]
    for genre in genre_names:
        Genre.objects.create(name=genre)

    for actor in range(len(actor_surnames)):
        Actor.objects.create(
            first_name=actor_names[actor],
            last_name=actor_surnames[actor]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney", ).update(last_name="Clooney")
    Actor.objects.filter(
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )
    # deleted
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return (
        Actor.objects
        .filter(last_name="Smith")
        .order_by("first_name")
    )


if __name__ == "__main__":
    main_query = main()
    print(main_query)
    print(Genre.objects.all())
    print(Actor.objects.all())
