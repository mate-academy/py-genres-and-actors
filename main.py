import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # create
    genre_data = [
        "Western",
        "Action",
        "Dramma"
    ]
    for name in genre_data:
        Genre.objects.create(name=name)

    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actors_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)
    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    # delete
    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()
    # read
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
