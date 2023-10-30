import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genre_name = ["Western", "Action", "Drama"]
    Genre.objects.bulk_create([Genre(name=name) for name in genre_name])

    actor_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlet", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlet", "Johansson"),
    ]
    Actor.objects.bulk_create(
        [Actor(first_name=first, last_name=last) for first, last in actor_data]
    )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlet").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
