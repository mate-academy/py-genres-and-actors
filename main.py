import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:

    # Creating records
    new_genres = ["Western", "Action", "Dramma"]
    for genre in new_genres:
        Genre.objects.create(name=genre)

    new_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for actor_first_name, actor_last_name in new_actors:
        Actor.objects.create(
            first_name=actor_first_name,
            last_name=actor_last_name
        )

    # Updating records
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    (Actor.objects.filter(first_name="Kianu")
     .update(first_name="Keanu", last_name="Reeves"))

    # Deleting records
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
