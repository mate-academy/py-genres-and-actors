import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


genres = ["Western", "Action", "Dramma"]

actors = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def main() -> QuerySet:

    for genre in genres:
        Genre.objects.create(
            name=genre
        )

    for actor_first, actor_second in actors:
        Actor.objects.create(
            first_name=actor_first,
            last_name=actor_second
        )

    genre = Genre.objects.get(
        name="Dramma"
    )
    genre.name = "Drama"
    genre.save()

    actor = Actor.objects.get(
        last_name="Klooney"
    )
    actor.last_name = "Clooney"
    actor.save()

    actor = Actor.objects.get(
        first_name="Kianu",
        last_name="Reaves"
    )
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    )
