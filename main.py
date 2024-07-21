import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genre_objects_create = ["Western", "Action", "Dramma"]
    for genre in genre_objects_create:
        Genre.objects.create(name=genre)

    actor_objects_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actor_objects_create:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    actor_objects_update = [
        (("George", "Klooney"), ("George", "Clooney")),
        (("Kianu", "Reaves"), ("Keanu", "Reeves"))
    ]

    for old_values, values_to_update in actor_objects_update:
        old_first_name, old_last_name = old_values
        new_first_name, new_last_name = values_to_update

        Actor.objects.filter(
            first_name=old_first_name,
            last_name=old_last_name
        ).update(first_name=new_first_name, last_name=new_last_name)

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
