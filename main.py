import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Drama"]
    for genre in genres_to_create:
        Genre.objects.create(name=genre)

    actors_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actors_to_create:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(
        name="Drama"
    )

    actors_to_update = [
        (("George", "Klooney"), ("George", "Clooney")),
        (("Kianu", "Reaves"), ("Keanu", "Reeves"))
    ]
    for old_actors_info, new_actors_info in actors_to_update:
        Actor.objects.filter(
            first_name=old_actors_info[0],
            last_name=old_actors_info[1]
        ).update(
            first_name=new_actors_info[0],
            last_name=new_actors_info[1]
        )

    Genre.objects.filter(name="Action",).delete()
    Actor.objects.filter(first_name="Scarlett",).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
