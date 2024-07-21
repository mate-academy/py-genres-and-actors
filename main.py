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
    for actor in actor_objects_create:
        first_name_, last_name_ = actor[0], actor[1]
        Actor.objects.create(
            first_name=first_name_,
            last_name=last_name_
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    actor_objects_update = [
        (("George", "Klooney"), ("George", "Clooney")),
        (("Kianu", "Reaves"), ("Keanu", "Reeves"))
    ]
    for actor in actor_objects_update:
        first_name_, last_name_, new_first_name, new_last_name = (
            actor[0][0],
            actor[0][1],
            actor[1][0],
            actor[1][1]
        )
        Actor.objects.filter(
            first_name=first_name_,
            last_name=last_name_
        ).update(first_name=new_first_name, last_name=new_last_name)

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
