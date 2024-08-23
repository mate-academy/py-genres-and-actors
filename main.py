import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Dramma"]
    actors_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for genre in genres_to_create:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    actors_to_update = {
        ("George", "Klooney"): {"last_name": "Clooney"},
        ("Kianu", "Reaves"): {"first_name": "Keanu", "last_name": "Reeves"},
    }

    for old_name, new_name in actors_to_update.items():
        old_first_name, old_last_name = old_name
        new_first_name = new_name.get("first_name", old_first_name)
        new_last_name = new_name.get("last_name", old_last_name)

        Actor.objects.filter(
            first_name=old_first_name,
            last_name=old_last_name
        ).update(
            first_name=new_first_name, last_name=new_last_name
        )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
