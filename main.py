import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def create_row() -> None:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )


def update_row() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )


def delete_row() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def get_sorted_actors() -> QuerySet:
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def main() -> QuerySet:
    create_row()
    update_row()
    delete_row()
    return get_sorted_actors()
