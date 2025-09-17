# pip install legacy-cgi
import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    # create
    for name in genres:
        Genre.objects.create(name=name)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
