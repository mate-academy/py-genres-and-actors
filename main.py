import init_django_orm  # noqa: F401

from django.core.management import call_command
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    # Create database tables directly from models
    call_command("migrate", run_syncdb=True, verbosity=0)

    # Create genres using loop
    genres = [
        "Western",
        "Action",
        "Dramma",
    ]
    for name in genres:
        Genre.objects.get_or_create(name=name)

    # Create actors using loop
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
        )

    # Update records
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney",
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(
        first_name="Keanu",
        last_name="Reeves",
    )

    # Delete records
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return required QuerySet
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
