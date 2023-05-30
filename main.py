import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actor_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    Genre.objects.bulk_create(
        [
            Genre(name=genre)
            for genre in genres
        ]
    )
    Actor.objects.bulk_create(
        [
            Actor(
                first_name=actor_first_name,
                last_name=actor_last_name,
            )
            for actor_first_name,
            actor_last_name in actor_data
        ]
    )
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()
    actors_ln_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return actors_ln_smith


if __name__ == "__main__":
    main()
