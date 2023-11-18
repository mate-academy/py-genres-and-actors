import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors_names = [("George", "Klooney"),
                    ("Kianu", "Reaves"),
                    ("Scarlett", "Keegan"),
                    ("Will", "Smith"),
                    ("Jaden", "Smith"),
                    ("Scarlett", "Johansson")]

    for genre_name in genres:
        Genre.objects.create(
            name=genre_name
        )
    for actor_first_name, actor_last_name in actors_names:
        Actor.objects.create(
            first_name=actor_first_name,
            last_name=actor_last_name
        )
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu",
                         last_name="Reaves").update(first_name="Keanu",
                                                    last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    actors_with_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return actors_with_smith
