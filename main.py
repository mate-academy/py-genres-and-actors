from django.db.models import QuerySet
from db.models import Genre, Actor, Actress


def main() -> QuerySet:

    genres = ["Western", "Action", "Dramma"]
    for name in genres:
        Genre.objects.create(name=name)

    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
    ]
    for actor_data in actors:
        Actor.objects.create(**actor_data)

    actresses = [
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]
    for actress_data in actresses:
        Actress.objects.create(**actress_data)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actress.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
