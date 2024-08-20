import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    list_genre = ["Western", "Action", "Dramma"]
    list_actor = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for genre_name in list_genre:
        Genre.objects.create(name=genre_name)

    for actor_name_surname in list_actor:
        Actor.objects.create(
            first_name=actor_name_surname[0],
            last_name=actor_name_surname[1]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    filtered_actor = (
        Actor.objects.filter(
            last_name="Smith",
        ).order_by("first_name")
    )

    return filtered_actor
