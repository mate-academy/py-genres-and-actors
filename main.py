import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main() -> None:
    genres = [
        "Western",
        "Action",
        "Dramma",
    ]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    # Create genres
    for name in genres:
        Genre.objects.create(name=name)

    # Create actors
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Update records
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu",
                                                    last_name="Reeves")

    # Delete records
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return actors sorted by first_name
    actors_with_last_name_smith = (Actor.objects.filter
                                   (last_name="Smith").order_by("first_name"))

    return actors_with_last_name_smith
