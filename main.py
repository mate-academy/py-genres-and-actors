import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

genres = ("Western", "Action", "Dramma")
actors = (
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
)


def main() -> QuerySet:
    filter_genre = Genre.objects.filter
    filter_actor = Actor.objects.filter

    for genre in genres:
        Genre.objects.create(name=genre)
    for name, surname in actors:
        Actor.objects.create(first_name=name, last_name=surname)

    filter_genre(name="Dramma").update(name="Drama")
    filter_actor(
        first_name="George", last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    filter_actor(
        first_name="Kianu", last_name="Reaves"
    ).update(
        first_name="Keanu", last_name="Reeves"
    )

    filter_genre(name="Action").delete()
    filter_actor(first_name="Scarlett").delete()

    return filter_actor(
        last_name="Smith"
    ).order_by(
        "first_name"
    )
