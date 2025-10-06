import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    for name in ["Western", "Action", "Dramma"]:
        Genre.objects.create(
        name=name,
    )

    actors = [
        ("George", "Klooney"), ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"), ("Will", "Smith"), ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for first, last in actors:
        Actor.objects.create(
            first_name=first,
            last_name=last,
        )

    update_drama_genre = Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    print(update_drama_genre)

    update_george = Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")
    print(update_george)

    kianu_update = Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(first_name="Keanu", last_name="Reeves")
    print(kianu_update)

    delete_genre = Genre.objects.filter(
        name="Action",
    ).delete()
    print(delete_genre)

    delete_all_scarletts = Actor.objects.filter(
        first_name="Scarlett",
    ).delete()
    print(delete_all_scarletts)

    to_return = Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
    return to_return
