import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Genre, Actor

def main() -> None:
    genres: list[str] = ["Western", "Action", "Dramma"]
    actors: list[tuple[str, str]] = [
        ("George", "Cloney"),
        ("Keanu", "Reevs"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Cloney").update(
        last_name="Clooney"
    )


if __name__ == "__main__":
    main()
