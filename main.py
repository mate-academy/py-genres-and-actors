import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Dramma"]
    for genre in genres_to_create:
        Genre.objects.create(
            name=genre
        )
    actors_to_create = [
        ("George", "Klooney"), ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"), ("Will", "Smith"),
        ("Jaden", "Smith")
    ]
    for first_name, last_name in actors_to_create:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    Genre.objects.get(
        name="Dramma"
    ).update(
        name="Drama"
    )
    Actor.objects.get(
        first_name="George",
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    )
    Actor.objects.get(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.get(
        name="Action"
    ).delete()
    queryset = Actor.objects.filter(
        first_name="Scarlett"
    )
    for el in queryset:
        el.delete()
    res_queryset = Actor.objects.filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    )
    return res_queryset
