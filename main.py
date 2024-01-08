import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]

    for genre in genres:
        Genre.objects.create(
            name=genre,
        )

    for first_parameter, second_parameter in actors:
        Actor.objects.create(
            first_name=first_parameter,
            last_name=second_parameter,
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    new_data = [("George", "Klooney", "George", "Clooney"),
                ("Kianu", "Reaves", "Keanu", "Reeves")]

    for (old_first_name, old_last_name,
         new_first_name, new_last_name) in new_data:

        Actor.objects.filter(
            first_name=old_first_name,
            last_name=old_last_name,
        ).update(
            first_name=new_first_name,
            last_name=new_last_name,
        )

    Genre.objects.filter(
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
