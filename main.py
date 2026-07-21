import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]

    for (name,) in genres:
        Genre.objects.create(name=name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genre_updates = [
        ({"name": "Dramma"}, {"name": "Drama"}),
    ]

    for filters, updates in genre_updates:
        Genre.objects.filter(**filters).update(**updates)

    actor_updates = [
        ({"last_name": "Klooney"}, {"last_name": "Clooney"}),
        ({"last_name": "Reaves"},
         {"first_name": "Keanu", "last_name": "Reeves"}),
    ]

    for filters, updates in actor_updates:
        Actor.objects.filter(**filters).update(**updates)

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
